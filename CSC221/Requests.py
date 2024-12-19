import requests

# List of items to be used as URL parameters
items = ['item1', 'item2', 'item3', 'item4']

# Base URL to which the items will be appended
base_url = 'https://google.com'

# Loop over each item and make a request
for item in items:
    # Construct the full URL
    url = base_url #+ item

    # Print the URL or make an HTTP request (using requests library for example)
    print(f"Making request to: {url}")

    # Uncomment below if you want to make actual requests
    response = requests.get(url)
    print(f"Response for {item}: {response.status_code}, {response.text}")
