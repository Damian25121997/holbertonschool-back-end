#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    Function
    """
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get('https://jsonplaceholder.typicode.com/users/')
    todos = todo.json()
    users = user.json()

    for id in users:
        if id['id'] == int(argv[1]):
            username = id['username']
    list = []

    for task in todos:
        dictionary = {}
        if task['userId'] == int(argv[1]):
            dictionary['username'] = username
            dictionary['task'] = task['title']
            dictionary['completed'] = task['completed']
            list.append(dictionary)
    dictionary_f = {}
    dictionary_f[int(argv[1])] = list
    json_f = json.dumps(dictionary_f)

    with open(argv[1] + '.json', 'w') as file:
        file.write(json_f)
