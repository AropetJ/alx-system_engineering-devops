#!/usr/bin/python3
"""A script that returns information about his/her TODO list progress.
"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    emp = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as infofile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in emp}, infofile)
