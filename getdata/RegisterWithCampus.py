import requests

'''
this gets SSO authentication failed
I think this is due to the temp token already have been used
for the mobile order login
and it's only valid once.



'''

url = "https://hangrybbapiprod-main.azurewebsites.net/api_user/registerwithcampusssotoken"

headers = {
    "accept": "*/*",
    "sessionid": "1681961592308",
    "content-type": "application/json",
    "api_key": "EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd",
    "accept-encoding": "gzip, deflate, br",
    "user-agent": "Transact/51 CFNetwork/1240.0.4 Darwin/20.6.0",
    "accept-language": "en-us",
    "content-length": "361"
}

data = {
    "userid": "0",
    "hash": "f000aac07ba8d370d10e52ae88bff09e260c81929096b77cfb66328faa78f77a",
    "os_type": "0",
    "app_bundle_name": "com.transact.mobileorder",
    "language": "EN",
    "temp_token": "196af72e3930482a000fba1eeebfee8850212e7da49fe01be495d4569b117544dbf51eff7b59ee90c9218a955fb4708a084ffa5dd591f2368289bd6976dfd0fd41",
    "campusid": "19"
}

response = requests.post(url, headers=headers, json=data, verify=False)

print(response.status_code)
print(response.content)
