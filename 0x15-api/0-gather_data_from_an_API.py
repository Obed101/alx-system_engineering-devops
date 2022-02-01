#!/usr/bin/python3
""" This script displays information about a user's tasks"""
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    users = requests.get(user_url).json()
    usr_tasks = requests.get(url).json()

    tasks_done = 0
    for task in usr_tasks:
        if task.get('completed'):
            tasks_done += 1

    def print_emp(tasks_done, usr_tasks, users):
        """ Prints Employees tasks done and total tasks """
        task_info = "Employee {} is done with tasks({}/{}):".format(
                users.get('name'), tasks_done, len(usr_tasks))
        print(task_info)
        for task in usr_tasks:
            if task.get('completed'):
                print("\t {}".format(task.get('title')))
    print_emp(tasks_done, usr_tasks, users)
