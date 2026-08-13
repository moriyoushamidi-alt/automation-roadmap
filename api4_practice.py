import requests
import json

response = requests.get("https://api.github.com/users/moriyoushamidi-alt")
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    
    my_data = {
        "login": data["login"],
        "public_repos": data["public_repos"],
        "created_at": data["created_at"]
    }
    
    with open("my_profile.json", "w") as file:
        json.dump(my_data, file)
    
    print("Saved to my_profile.json")
else:
    print(f"Request failed with status code: {response.status_code}")