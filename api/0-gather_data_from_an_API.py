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
    todo_json = todo.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    users_json = users.json()
    id_u = int(argv[1])
    total_number_task = 0
    number_of_done_tasks = 0
    task_title = []

    for user in users_json:
        if user.get('id') == id_u:
            name_e = user.get('name')
            break

    for task in todo_json:
        if task.get('userId') == id_u:
            total_number_task += 1
            if task.get('completed') is True:
                number_of_done_tasks += 1
                task_title.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name_e, number_of_done_tasks, total_number_task))
    for x in task_title:
        print('\t {}'.format(x))
