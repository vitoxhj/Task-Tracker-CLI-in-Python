import json
import os
from time import sleep

def create_json(arquive,dados):
    if not os.path.exists(arquive):
        with open(arquive, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    else:
        return
def save_tasks(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def create(tasks):
    name = str(input('Task:'))
    new_id = 1
    while any(task['id'] == new_id for task in tasks):
        new_id += 1

    info = {
        'id': new_id,
        'name': name,
        'completed': False,
        'In_progress':False
    }
    tasks.append(info)
    save_tasks(tasks)
    print('Task added successfully!')
    sleep(1)

def update(tasks):
    id = int(input('ID:'))
    for task in tasks:
        if task['id'] == id:
            print(f'old: {task['name']}')
            new = str(input('New:'))
            task['name'] = new
            save_tasks(tasks)
            print('Task updated successfully!')
            sleep(1)
            return
    print('ID not found!')
    sleep(1)
    return

def delete(tasks):
    id = int(input('ID:'))
    for task in tasks:
        if task['id'] == id:
            print(f'task: {task['name']}')
            confirm = input(('Really delete this task?[yes/no]:')).strip().lower()
            if confirm == 'no':
                return
            elif confirm == 'yes':
                tasks.remove(task)
                save_tasks(tasks)
                print('Task deleted successfully!')
                sleep(1)
                return
            else:
                print('type only yes or no!')
                sleep(1)
                return
    print('ID not found!')
    sleep(1)
    return

def mark(tasks):
    task_id = int(input('ID:'))
    for task in tasks:
        if task['id'] == task_id:
            print(f'Task: {task['name']}')
            print('1-Mark completed\n2-Mark in-progress\n3-Mark as not started')
            print('='*30)
            option = int(input('->'))
            if option < 1 or option > 3:
                print('Option unavailable')
                sleep(1)
                return
            elif option == 1:
                task['completed'] = True
                task['In_progress'] = False

            elif option == 2:
                task['In_progress'] = True
                task['completed'] = False
            elif option == 3:
                task['In_progress'] = False
                task['completed'] = False

            save_tasks(tasks)
            print('Task marked successfully!')
            sleep(1)
            return
    print('ID not found!')
    sleep(1)
    return

def show_task(task):
    print(f'ID: {task['id']}\nTask: {task['name']}')
    if task['completed']:
        print('Completed: ✅')
    else:
        print('Completed: ❌')
    if task['In_progress']:
        print('in-progress: ✅')
    else:
        print('in-progress: ❌')
    print('-'*30)

def list_tasks(tasks):
    if not tasks:
        print('Not tasks in manager!')
        return
    for task in tasks:
        show_task(task)

def list_tasks_completeds(tasks):
    if not tasks:
        print('Not tasks in manager!')
        return
    found = False
    for task in tasks:
        if task['completed']:
            found = True
            show_task(task)
    if not found:
        print('No completed tasks')

def list_tasks_not_completeds(tasks):
    if not tasks:
        print('Not tasks in manager!')
        return
    found = False
    for task in tasks:
        if not task['completed']  and not task['In_progress']:
            found = True
            show_task(task)
    if not found:
        print('No not completed tasks')

def list_tasks_in_progress(tasks):
    if not tasks:
        print('Not tasks in manager!')
        return
    found = False
    for task in tasks:
        if task['In_progress']:
            found = True
            show_task(task)
    if not found:
        print('No in-progress tasks')
                

