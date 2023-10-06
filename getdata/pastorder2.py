import requests
import json

# Define the URL
url = "https://mobileorderprodapi.transactcampus.com/api_user/getpastorders"

# Define the JSON payload
payload = {
    "userid": "46210",
    "campusid": "19"
}

# Define custom headers
headers = {
    "Content-Type": "application/json",
    "sessionid": "1695142470976",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Transact%20Prod/237 CFNetwork/1240.0.4 Darwin/20.6.0",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Accept-Language": "en-us",
    "Content-Length": "45",
    "api_key": "EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd",
    "login_token": "46210d446873374337f1b95dc028fb35796084b3928cee76eee2538cea66e7cfa47aa79e6cda5b65e6fa9c1535d5beabda1d53842e295af95318fb5337eeb81c84d93"
}

# Disable SSL certificate verification (not recommended for production)
response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)

# Check the response
if response.status_code == 200:
    # Request was successful
    print("Request was successful!")
    print("Response:")
    print(response.text)
else:
    # Request failed
    print(f"Request failed with status code {response.status_code}")
    print("Response:")
    print(response.text)
