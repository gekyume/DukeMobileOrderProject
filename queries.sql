-- Get person’s most expensive order

CREATE VIEW expensive_orders AS
SELECT UserID, max(OrderItems.price_base) as price
FROM OrderItems
GROUP BY OrderItems.UserID
HAVING Count(OrderItems.name) > 0
JOIN
SELECT UserID, price_base as price, name
FROM OrderItems;

-- Get person’s cheapest order

CREATE VIEW cheapest_orders AS
SELECT User.UserID, min(OrderItems.price_base) as price
FROM OrderItems, User
WHERE OrderItems.UserID = User.UserID
GROUP BY User.UserID
HAVING Count(OrderItems.name) > 0
JOIN
SELECT UserID, price_base as price, name
FROM OrderItems


-- Count of orders per user

CREATE VIEW order_counts AS
SELECT User.UserID, count(*)
FROM OrderItems
GROUP BY User.UserID

-- Longest ever wait for an order

CREATE VIEW longest_wait AS
SELECT User.UserID, max(kitchen_prep_minutes)
FROM OrderItems
GROUP BY User.UserID

-- Most frequented Cafeteria

AggregatedOrders AS (
    SELECT
        userid,
        cafeteriaid,
        COUNT(orderid) as order_count
    FROM
        OrderDetails
    GROUP BY
        userid,
        cafeteriaid
);

MaxOrders AS (
    SELECT
        userid,
        MAX(order_count) as max_order_count
    FROM
        AggregatedOrders
    GROUP BY
        userid
);

CREATE VIEW most_frequented AS
SELECT
    a.userid,
    a.cafeteriaid,
    a.order_count
FROM
    AggregatedOrders a
JOIN
    MaxOrders m
ON
    a.userid = m.userid AND a.order_count = m.max_order_count;

-- Week with most orders for each user

WeeklyOrders AS (
    SELECT
        userid,
        EXTRACT(YEAR FROM order_local_date) as order_year,
        EXTRACT(WEEK FROM order_local_date) as order_week,
        COUNT(orderid) as order_count
    FROM
        OrderID
    GROUP BY
        userid,
        EXTRACT(YEAR FROM order_local_date),
        EXTRACT(WEEK FROM order_local_date)
),

MaxWeeklyOrders AS (
    SELECT
        userid,
        MAX(order_count) as max_order_count
    FROM
        WeeklyOrders
    GROUP BY
        userid
);


CREATE VIEW most_orders AS
SELECT
    w.userid,
    w.order_year,
    w.order_week,
    w.order_count
FROM
    WeeklyOrders w
JOIN
    MaxWeeklyOrders m
ON
    w.userid = m.userid AND w.order_count = m.max_order_count;
