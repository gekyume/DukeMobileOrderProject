import json
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://YOUR_USER:YOUR_PASSWORD@YOUR_RDS_ENDPOINT:YOUR_PORT/YOUR_DATABASE_NAME"

engine = create_engine(DATABASE_URL)

def lambda_handler(event, context):
    # Ensure there's at least one message
    if not event['Records']:
        return

    # Extract the message content from the SQS event
    message_content = event['Records'][0]['body']
    data = json.loads(message_content)

    # Extract the required data from the event
    orders = data.get("orders", [])
    users = extract_users_updated(orders)
    locations = extract_locations(orders)
    cafeteria_index = extract_cafeteria_index(orders)
    mains_index = extract_mains_index(orders)
    order_items = extract_order_items(orders)
    order_details = extract_order_details(orders)

    # Use the connection to execute the insert statements
    with engine.connect() as conn:
        insert_users(conn, users)
        insert_locations(conn, locations)
        insert_cafeteria_index(conn, cafeteria_index)
        insert_mains_index(conn, mains_index)
        insert_order_items(conn, order_items)
        insert_order_details(conn, order_details)

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully!')
    }

# The insert functions remain largely unchanged, but with SQLAlchemy's methods
def insert_users(connection, users):
    insert_query = text("""INSERT INTO User(UserID, NetID, FirstName, LastName, Email, user_number_of_orders) 
                           VALUES (:UserID, :NetID, :FirstName, :LastName, :Email, :user_number_of_orders) 
                           ON CONFLICT (UserID) DO NOTHING;""")
    connection.execute(insert_query, users)

def insert_locations(connection, locations):
    insert_query = text("""INSERT INTO Location(LocationName, LocationID, Address) 
                           VALUES (:LocationName, :LocationID, :Address) 
                           ON CONFLICT (LocationID) DO NOTHING;""")
    connection.execute(insert_query, locations)

def insert_cafeteria_index(connection, cafeteria_index):
    insert_query = text("""INSERT INTO CafeteriaIndex(cafeteriaid, Name, LocationID, Category, LogoPhotoID) 
                           VALUES (:cafeteriaid, :Name, :LocationID, :Category, :LogoPhotoID) 
                           ON CONFLICT (cafeteriaid) DO NOTHING;""")
    connection.execute(insert_query, cafeteria_index)

def insert_mains_index(connection, mains_index):
    insert_query = text("""INSERT INTO MainsIndex(cafeteriaid, menu_itemid, menu_sectionid, name, price_base) 
                           VALUES (:cafeteriaid, :menu_itemid, :menu_sectionid, :name, :price_base) 
                           ON CONFLICT (cafeteriaid, menu_itemid) DO NOTHING;""")
    connection.execute(insert_query, mains_index)

def insert_order_items(connection, order_items):
    insert_query = text("""INSERT INTO OrderItems(userid, orderid, itemid, menu_itemid) 
                           VALUES (:userid, :orderid, :itemid, :menu_itemid)""")
    connection.execute(insert_query, order_items)

def insert_order_details(connection, order_details):
    insert_query = text("""INSERT INTO OrderDetails(userid, orderid, cafeteriaid, location_subtotal, order_local_date, order_local_time, number_of_items, kitchen_prep_minutes) 
                           VALUES (:userid, :orderid, :cafeteriaid, :location_subtotal, :order_local_date, :order_local_time, :number_of_items, :kitchen_prep_minutes)""")
    connection.execute(insert_query, order_details)

def extract_users_updated(orders):
    users_list = []

    for order in orders:
        user = {
            "UserID": order.get('userid', None),
            "NetID": None,
            "FirstName": None,
            "LastName": None,
            "Email": None,
            "user_number_of_orders": order.get('user_number_of_orders', None)
        }
        users_list.append(user)

    # Deduplicate users based on UserID
    seen_users = set()
    deduplicated_users = []
    for user in users_list:
        if user["UserID"] not in seen_users:
            seen_users.add(user["UserID"])
            deduplicated_users.append(user)

    return deduplicated_users


def extract_locations(orders):
    locations_list = []

    for order in orders:
        location = {
            "LocationName": None,
            "LocationID": order.get('locationid', None),
            "Address": None
        }
        locations_list.append(location)

    # Deduplicate locations based on LocationID
    seen_locations = set()
    deduplicated_locations = []
    for location in locations_list:
        if location["LocationID"] not in seen_locations:
            seen_locations.add(location["LocationID"])
            deduplicated_locations.append(location)

    return deduplicated_locations


def extract_cafeteria_index(orders):
    cafeteria_list = []

    for order in orders:
        cafeteria = {
            "cafeteriaid": order.get('cafeteriaid', None),
            "Name": None,
            "LocationID": order.get('locationid', None),
            "Category": None,
            "LogoPhotoID": None
        }
        cafeteria_list.append(cafeteria)

    # Deduplicate based on cafeteriaid
    seen_cafeterias = set()
    deduplicated_cafeterias = []
    for cafeteria in cafeteria_list:
        if cafeteria["cafeteriaid"] not in seen_cafeterias:
            seen_cafeterias.add(cafeteria["cafeteriaid"])
            deduplicated_cafeterias.append(cafeteria)

    return deduplicated_cafeterias


def extract_mains_index(orders):
    mains_list = []

    for order in orders:
        for item in order.get('items', []):
            main = {
                "cafeteriaid": order.get('cafeteriaid', None),
                "menu_itemid": item.get('menu_itemid', None),
                "menu_sectionid": item.get('menu_sectionid', None),
                "name": item.get('name', None),
                "price_base": item.get('price_base', None)
            }
            mains_list.append(main)

    # Deduplicating based on combination of cafeteriaid and menu_itemid
    seen_mains = set()
    deduplicated_mains = []
    for main in mains_list:
        key = (main["cafeteriaid"], main["menu_itemid"])
        if key not in seen_mains:
            seen_mains.add(key)
            deduplicated_mains.append(main)

    return deduplicated_mains


def extract_order_items(orders):
    order_items_list = []

    for order in orders:
        for item in order.get('items', []):
            order_item = {
                "userid": order.get('userid', None),
                "orderid": order.get('orderid', None),
                "itemid": item.get('itemid', None),
                "menu_itemid": item.get('menu_itemid', None)
            }
            order_items_list.append(order_item)

    return order_items_list


def extract_order_details(orders):
    order_details_list = []

    for order in orders:
        order_detail = {
            "userid": order.get('userid', None),
            "orderid": order.get('orderid', None),
            "cafeteriaid": order.get('cafeteriaid', None),
            "location_subtotal": order.get('location_subtotal', None),
            "order_local_date": order.get('order_local_date', None),
            "order_local_time": order.get('order_local_time', None),
            "number_of_items": order.get('number_of_items', None),
            "kitchen_prep_minutes": order.get('kitchen_prep_minutes', None)
        }
        order_details_list.append(order_detail)

    return order_details_list
