import requests

"""Basic API call for the ISS location"""
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
response.raise_for_status()


data = response.json()
print(data)
