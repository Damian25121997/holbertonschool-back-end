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
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(argv[1]))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todos = todo.json()
    users = user.json()
    new_list = []
    
    print(new_list)
    dictionary = {
            # # 'task': '{}'.format(todos.get('title')),
            # # 'completed': '{}'.format(todos.get('completed')),
            # # 'username': '{}'.format(users.get('username'))
            }
    dictionary['task'] = '{}'.format(todos.get('title'))
    dictionary['completed'] = '{}'.format(todos.get('completed'))
    dictionary['username'] = '{}'.format(todo.get('username'))
    dictionary2 = dictionary.copy()
    new_list.append(dictionary2)
    print(new_list)
        
#    with open('{}.json'.format(argv[1]), 'w') as json_file:
#        temp = {}
#        for key, val in temp.items():
#            temp[key] = todos
#        json.dump(todos, json_file)