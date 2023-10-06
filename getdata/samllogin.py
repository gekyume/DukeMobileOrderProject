import requests

url = "https://mobileorderprodapi.transactcampus.com/api_user/samllogin"
params = {
    "campusid": "19",
    "api_key": "EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd"
}

headers = {
    "Host": "mobileorderprodapi.transactcampus.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}

response = requests.get(url, params=params, headers=headers)

# Print the response code, headers, and content
print("Response Code:", response.status_code)
print("Headers:", response.headers)
print("Content:", response.text)
