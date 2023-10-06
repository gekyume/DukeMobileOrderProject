import requests

# set the API endpoint URL
url = "https://hangrybbapiprod-main.azurewebsites.net/api_user/loginwithtoken"

# set the headers for the request
headers = {
    "accept": "*/*",
    "sessionid": "1681959536568",
    "content-type": "application/json",
    "content-length": "510",
    "api_key": "EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd",
    "login_token": "46210fb4254c2220825657f53b3287a497dbbcf360101cc70a173294bd3b52b7bcb1eca8a4c41d56f1b8b9b1176953e3d418706617f7e0bd93cbe153aa0283366cf50",
    "user-agent": "Transact/51 CFNetwork/1240.0.4 Darwin/20.6.0",
    "accept-language": "en-us",
    "accept-encoding": "gzip, deflate, br",
}

# set the request data
data = {
    "device_model": "iPhone SE 2nd Gen / Aaron's iphone / iPhone12,8",
    "campusid": "19",
    "on_launch": "1",
    "app_version": "3.1.0",
    "userid": "46210",
    "carrier_name": "T-Mobile",
    "accessibility_mode": "0",
    "device_name": "Aaron's iphone",
    "push_enabled": "1",
    "os_language": "en-US",
    "timezone": "EST",
    "app_bundle_name": "com.transact.mobileorder",
    "os_version": "14.8.1",
    "push_token": "F8FCFED9-7E36-44E0-A569-A3DB2D46E007-2455-0000012EFBE679AB",
    "os_type": "0",
}

# make the POST request
response = requests.post(url, headers=headers, json=data, verify=False)

# print the response status code and content
print(response.status_code)
print(response.content)
