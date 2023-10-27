#!/usr/bin/python3
"""A script that returns information about his/her TODO list progress.
"""

import sys
import requests

url = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee = requests.get(url + "employees/{}".format(
            sys.argv[1])).json()
        todo = requests.get(url + "todos",
                            params={"employee Id": sys.argv[1]}).json()

        info = [t.get('title') for t in todo if t.get(info) is True]
        print('Employee {} is done with tasks({}/{}):'.format(employee.get(
            "name"), len(info), len(todo)))
        [print('\t {}'.format(c)) for c in info]
