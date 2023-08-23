import requests
import json

base_url = "http://localhost:8000"


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


def get_category():
    url = f"{base_url}/category-list/"
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def get_category_parent(category_id):
    url = f"{base_url}/category-parent-list/{category_id}/"
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)


def get_course_video(course_id):
    url = f"{base_url}/course-list/{course_id}/"
    response = requests.get(url)
    response.raise_for_status()
    for i in json.loads(response.text):
        print(i)
        return [v['video'] for v in i['course_video']]
