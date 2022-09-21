import requests

#response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
response = requests.get("https://api.open-notify.org/astros.json")

print(response.status_code)