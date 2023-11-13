import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <user_id>")
    sys.exit(1)

id = sys.argv[1]

# Fetch user data and tasks
try:
    user_request = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    tasks_request = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')

    user_request.raise_for_status()
    tasks_request.raise_for_status()

    user_data = user_request.json()
    tasks_data = tasks_request.json()

    username = user_data.get('username', 'Unknown')

    filename = f"{id}.csv"

    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks_data:
            csv_writer.writerow([id, username, task["completed"], task["title"]])

except requests.exceptions.RequestException as e:
    print(f"Error: Unable to fetch data - {e}")
except Exception as e:
    print(f"Error: An unexpected error occurred - {e}")
