import requests

url = "https://this-domain-really-does-not-exist-98765.com"

try:
     response=requests.get (url, timeout=10)
     print(response.status_code)

except requests.exceptions.RequestException as error:
     print(f"Could not connect: {error}")      