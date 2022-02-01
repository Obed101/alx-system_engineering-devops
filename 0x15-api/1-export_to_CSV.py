#!/usr/bin/python3
""" Exporting data to CSV fromat """
import csv
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    task_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            id)
    tasks = requests.get(task_url).json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    users = requests.get(user_url).json()
    csv_file = "{}.csv".format(id)

    with open(csv_file, 'w', newline='') as file:
        convert = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            convert.writerow(id, users.get('username'), task.get('completed'),
                    task.get('title'))
