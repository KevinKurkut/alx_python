"""import neessary modules
requests, json , sys"""
import requests
import sys
import json
"""function to perform required tasks"""
def tasks(user_id):
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    tasks_request = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

    if user_info.status_code != 200 or tasks_request.status_code != 200:
        print(f"Error: Unable to retrieve data for user {user_id}")
        return None

    user_info = json.loads(user_info.text)
    tasks = json.loads(tasks_request.text)
    """combine user tasks with todos"""
    for task in tasks:
        task["username"] = user_info["username"]

    return tasks

def export_to_json(user_id, tasks):
    if not tasks:
        print(f"No tasks found for user {user_id}")
        return

    filename = f"{user_id}.json"

    data = {str(user_id): [{"task": task["title"], "completed": task["completed"], "username": task["username"]} for task in tasks]}

    # Write to JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_tasks = tasks(user_id)

    export_to_json(user_id, user_tasks)
