#When I use the JSESSIONID from samllogin it gives me a timeout issue

import requests

# Define the URL and query parameters
url = "https://shib.oit.duke.edu/idp/profile/SAML2/Redirect/SSO"
params = {
    "execution": "e1s1",
    "_eventId_proceed": "1"
}

# Define the headers
headers = {
    "Host": "shib.oit.duke.edu",
    "Origin": "https://shib.oit.duke.edu",
    "Cookie": "JSESSIONID=17BA65777766203602C5066CA13EFF03; lastSuccessType=netid",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Accept-Language": "en-us",
    "Referer": "https://shib.oit.duke.edu/idp/authn/external?conversation=e1s1",
    "Accept-Encoding": "gzip, deflate, br"
}

# Make the HTTP GET request
response = requests.get(url, params=params, headers=headers, verify=False)

# Print the response
print("Response Code:", response.status_code)
print("Response Content:")
print(response.text)
