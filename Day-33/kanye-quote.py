import requests

"""Basic API call for the Kanye Quotes"""
url = "https://api.kanye.rest"
response = requests.get(url)
response.raise_for_status()


data = response.json()
print(data)
