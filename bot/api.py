import requests
import json

base_url = "http://localhost:8000/api"


def user_create(username, name, user_id):
    url = f"{base_url}/user-create/"
    get = requests.get(url).text
    date = json.loads(get)
    user_exist = False
    if date[0]["chat_id"] == user_id:
        user_exist = True
        return "user is exist"
    if user_exist == False:
        response = requests.post(url=url, data={"username": username, "first_name": name, "chat_id": user_id})
        if response.status_code == 201:
            return "Create User"
        else:
            return "Error creating user"
