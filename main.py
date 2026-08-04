import os
from time import sleep
import json
import functions



def main():
    #create json
    functions.create_json('tasks.json', [])

    #open json
    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)

    while True:
        #Interface
        try:
            sleep(0.5)
            print('='*30)
            print('TASK MANAGER'.center(30))
            print('='*30)
            print('1-add\n2-update\n3-delete\n4-mark\n5-list\n6-completed list\n7-not completed list\n8-list in progress\n9-exit')
            print('='*30)
            option = int(input('->'))
            #Erro
            if option <= 0 or option >= 10:
                print('option unavailable')
                sleep(1)
            #Create a task
            elif option == 1:
                functions.create(tasks)

            #update a task
            elif option == 2:
                functions.update(tasks)

            #Delete a task
            elif option == 3:
                functions.delete(tasks)

            #Mark a task
            elif option == 4:
                functions.mark(tasks)

            #List a tasks
            elif option == 5:
                functions.list_tasks(tasks)

            #List completed tasks
            elif option == 6:
                functions.list_tasks_completeds(tasks)

            #List not completed tasks
            elif option == 7:
                functions.list_tasks_not_completeds(tasks)

            #List in-progress tasks
            elif option == 8:
                functions.list_tasks_in_progress(tasks)

            elif option == 9:
                print('EXIT PROGRAM')
                return
        except ValueError:
            print('Value error')
            sleep(1)

if __name__ == '__main__':
    main()