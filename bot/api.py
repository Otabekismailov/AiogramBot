import requests
import json

base_url = "http://localhost:8000/api"


def user_create(username, name, user_id):
    url = f"{base_url}/user-create"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        print(i)
        if i["user_id"] == user_id:
            user_exist = True
            return "User is exist"
        else:
            requests.post(url=url, data={"username": username, "first_name": name, "user_id": user_id, })
            return "Create,User"


print(user_create("Otabek", "Otabek", "123"))
