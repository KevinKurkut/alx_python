#!/usr/bin/python3
"""import requests and json modules"""
import json
import requests
"""initialize store object"""
all_tasks = {}
for user_id in range(1, 11):
    request = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    data = request.json()

    tasks = []

    for item in data:
        tasks.append({"username": f"USER_{user_id}", "task": item.get('title'), "completed": item.get('completed')})

    all_tasks[str(user_id)] = tasks
json_file = "2.json"

with open(json_file, mode='w') as file:
    json.dump(all_tasks, file)
