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
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    id_u = int(argv[1])
    total_number_task = 0
    number_of_done_tasks = 0
    task_title = []

    for task in todo:
        if task.get('userId') == id_u:
            total_number_task += 1
            if task.get('completed') is True:
                number_of_done_tasks += 1
                task_title.append(task.get('title'))

    for user in users:
        if user.get('id') == id_u:
            name_e = user.get('name')

    print('Employee {} is done with tasks({}/{}):'
          .format(name_e, number_of_done_tasks, total_number_task))
    for x in task_title:
        print('\t {}'.format(x))
