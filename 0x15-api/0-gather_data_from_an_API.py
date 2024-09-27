import requests
import sys

def get_employee_todo_progress(employee_id):
    user_url_api = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url_api = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url_api)
    if user_response.status_code != 200:
        print("erorr")
        return
    user_data =  user_response.json()

    todo_response = requests.get(todo_url_api)
    if todo_response.status_code != 200:
        print("erorr")
        return
    todo_data = todo_response.json()

    #processing data
    employee_name = user_data['name']
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_of_completed = len(completed_tasks)

    print(f"Employee {employee_name} id done with tasks({num_of_completed}\{total_tasks}):")
    for tasks in completed_tasks:
        print(f"\t {tasks['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
