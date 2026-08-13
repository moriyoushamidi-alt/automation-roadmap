import requests

response = requests.get("https://this-domain-really-does-not-exist-98765.com")
print(response.status_code)

if response.status_code== 200:
    data=response.json()
    print(data["login"])

else:
    print(f"Request failed with status code: {response.status_code}")