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

    final_dictionary = {}
    for id in users:
        list = []
        for task in todos:
            dictionary = {}
            if id['id'] == task['userId']:
                dictionary['username'] = id['username']
                dictionary['task'] = task['title']
                dictionary['completed'] = task['completed']
                list.append(dictionary)
        final_dictionary[id['id']] = list
    with open('todo_all_employees.json', 'w') as file:
        json_file = json.dumps(final_dictionary)
        file.write(json_file)
