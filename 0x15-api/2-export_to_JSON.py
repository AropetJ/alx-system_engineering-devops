#!/usr/bin/python3
"""A script that returns information about his/her TODO list progress.
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    user_id = sys.argv[1]
    emp_id = requests.get(url + "users/{}".format(user_id)).json()
    emp_name = emp_id.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as infofile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": emp_name
            } for t in todos]}, infofile)
