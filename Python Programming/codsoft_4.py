import pickle
import os

tasksfile='tasks.pkl'

def load_tasks():
    if os.path.exists(tasksfile):
        with open(tasksfile,'rb') as file:
            try:
                return pickle.load(file)
            except (pickle.PickleError,EOFError):
                print("Error")
                return []
    return []

def save_tasks(tasks):
    try:
        with open(tasksfile,'wb') as file:
            pickle.dump(tasks,file)
    except IOError:
        print("Error")

def add_task(tasks):
    task=input("Enter the task description:").strip()
    if task:
        tasks.append({'description':task,'completed':False})
        print("Task added.")
    else:
        print("Task is empty")

def update_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    for idx,task in enumerate(tasks):
        status="Done" if task['completed'] else "Not done"
        print(f"{idx + 1}. {task['description']}-{status}")
    
    try:
        index=int(input("Enter the task number to update:"))-1
        if 0<=index<len(tasks):
            task=tasks[index]
            task['completed']=not task['completed']
            print("Task updated")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def delete_task(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    for idx,task in enumerate(tasks):
        status="Done" if task['completed'] else "Not done"
        print(f"{idx + 1}. {task['description']}-{status}")

    try:
        index=int(input("Enter the task number to delete:"))-1
        if 0<=index<len(tasks):
            confirmation=input(f"Are you sure you want to delete the task '{tasks[index]['description']}'? (yes/no): ").strip().lower()
            if confirmation=='yes':
                tasks.pop(index)
                print("Task deleted")
            else:
                print("Task deletion canceled")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def main():
    tasks=load_tasks()
    
    while True:
        print("To-Do List Menu:-")
        print("1.Add Task")
        print("2.Update Task")
        print("3.Delete Task")
        print("4.Exit")

        choice=input("Enter your choice:").strip()

        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            update_task(tasks)
        elif choice=='3':
            delete_task(tasks)
        elif choice=='4':
            save_tasks(tasks)
            print("Thank You")
            break
        else:
            print("Invalid choice.")
main()
