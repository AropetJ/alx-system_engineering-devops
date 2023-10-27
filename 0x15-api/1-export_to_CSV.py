"""A script that returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    userId = sys.argv[1]
    empReq = requests.get(url + "users/{}".format(userId)).json()
    userName = empReq.get("userName")
    taskReq = requests.get(url + "todos",
                            params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, userName, t.get("completed"), t.get("title")]
         ) for t in taskReq]
