#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""


import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    Function
    """
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(argv[1]))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todos = todo.json()
    users = user.json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        csvfile_2 = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for row in todos:
            csvfile_2.writerow([int(argv[1]), users.get('username'),
                                row.get('completed'), row.get('title')])
