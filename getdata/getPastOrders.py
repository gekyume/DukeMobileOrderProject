import requests

# Define the URL
url = "https://mobileorderprodapi.transactcampus.com/api_user/getpastorders"

# Define the headers
headers = {
    "Host": "mobileorderprodapi.transactcampus.com",
    "sessionid": "1695179636511",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Transact%20Prod/237 CFNetwork/1240.0.4 Darwin/20.6.0",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Language": "en-us",
    "Content-Length": "45",
    "api_key": "EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd",
    "login_token": "4621082cc67ec41c6af09bdd0ab498323f40a241a9dc4aa07946ce650255344b9ef207e0b8c75512a145eaee3d7215d42c9a1256375cc8c67282ba17f183bd20a62dd"
}

# Define the JSON data
data = {
    "userid": "46210",
    "campusid": "19"
}

# Send the POST request
response = requests.post(url, json=data, headers=headers, verify=False)

# Check the response
if response.status_code == 200:
    print("Request was successful")
    print("Response:")
    print(response.text)
else:
    print("Request failed with status code:", response.status_code)
