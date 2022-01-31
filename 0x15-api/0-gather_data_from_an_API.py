#!/usr/bin/python3
""" This script displays information about a user's tasks"""
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    url = f'https://jsonplaceholder.typicode.com/todos/{id}'
    usr_tasks = requests.get(url).json()
    user_url = f'https://jsonplaceholder.typicode.com/?userId={id}'
    if requests.get(user_url).status_code == 200:
        users = requests.get(user_url).json()

    tasks_done = 0
    for task in usr_tasks.values():
        if task == "completed":
            tasks_done += 1


    def print_emp(tasks_done, usr_tasks):
        """ Prints Employees tasks done and total tasks """
        task_info = "Employee {} is done with tasks({}/{}):".format(
                users.get('name'), tasks_done, len(usr_tasks))
        print(task_info)
        for task in usr_tasks.values():
            if task == "completed":
                print(f"\t {usr_tasks.get('title')}")
    print_emp(tasks_done, usr_tasks)
