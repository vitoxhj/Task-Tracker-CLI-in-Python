import json
import os
from time import sleep

def create_json(arquive,dados):
    if not os.path.exists(arquive):
        with open(arquive, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    else:
        return

def create(tasks):
    name = str(input('Task:'))
    info = {
        'id': len(tasks)+1,
        'name': name,
        'completed': False,
        'In_progress':False
    }
    tasks.append(info)

    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
    print('Task added successfully!')
    sleep(1)

def update(tasks):
    id = int(input('ID:'))
    for task in tasks:
        if task['id'] == id:
            print(f'old: {task['name']}')
            new = str(input('New:'))
            task['name'] = new
            with open('tasks.json', 'w', encoding='utf-8') as f:
                json.dump(tasks, f, indent=4, ensure_ascii=False)
            print('Task updated successfully!')
            sleep(1)
            return
    print('ID not found!')
    sleep(1)
    return