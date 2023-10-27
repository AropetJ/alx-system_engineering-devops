#!/usr/bin/python3
"""A script that returns information about his/her TODO list progress.
"""
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    emp_req = requests.get(url + "users/{}".format(sys.argv[1])).json()
    task_req = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in task_req if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        emp_req.get("name"), len(completed), len(task_req)))
    [print("\t {}".format(c)) for c in completed]
