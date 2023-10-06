import requests

# Define the URL
url = "https://mobileorderprodapi.transactcampus.com/api_user/samllogin?campusid=19&api_key=EF4yhUx3g23K7BeVpxG45UWMe4aB5hVXhTGmD9HH9TYBGWbmhd"

# Define headers to mimic a browser request
headers = {
    'Host': 'mobileorderprodapi.transactcampus.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
}

# Send a GET request with the custom headers
response = requests.get(url, headers=headers, verify=False)

# Check the response status code
if response.status_code == 200:
    # The request was successful
    print("Request was successful.")

    # Check if the response is a redirect (HTTP status code 302)
    if response.history:
        # Get the final URL after following the redirects
        final_url = response.url
        print("Final URL:", final_url)

        # Send a GET request to the final URL
        final_response = requests.get(final_url, verify=False)

        # You can access the content of the final response
        print("Final Response Content:", final_response.text)
    else:
        # No redirect, print the response content
        print("Response Content:", response.text)
elif response.status_code == 403:
    # Handle the 403 Forbidden error here
    print("Access denied. You don't have permission to access this resource.")
else:
    # Handle other status codes as needed
    print(f"Request failed with status code: {response.status_code}")

# Print the response details
print("Response Status Code:", response.status_code)
print("Response:")
print(response.text)
