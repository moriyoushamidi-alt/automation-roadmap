import requests

response=requests.get("https://api.github.com/users/moriyoushamidi-alt")
print(response.status_code)

data=response.json()
print(data["created_at"])
print(data["followers"])
print(data["type"])
