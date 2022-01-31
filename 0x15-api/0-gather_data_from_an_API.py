#!/usr/bin/python3
""" This script displays information about a user's tasks"""
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    user_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    url = f'https://jsonplaceholder.typicode.com/todos?userId={id}'
    users = requests.get(user_url).json()
    usr_tasks = requests.get(url).json()

    tasks_done = 0
    for task in usr_tasks:
        if task == "completed":
            tasks_done += 1

    def print_emp(tasks_done, usr_tasks, users):
        """ Prints Employees tasks done and total tasks """
        for user in users:
            print(user)
            if user.get('userId'):
                task_info = "Employee {} is done with tasks({}/{}):".format(
                        user.get('name'), tasks_done, len(usr_tasks))
                print(task_info)
                break
        for task in usr_tasks:
            if task.get('completed'):
                print(f"\t {task.get('title')}")
    print_emp(tasks_done, usr_tasks, users)
