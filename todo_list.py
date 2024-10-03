my_tasks = []
completed_tasks = []
def addTask():
    while True:
        task_to_add = input("Enter the task(s) you need to complete, and enter 'done' when finished: ")
        if task_to_add == 'done':
            break
        else:
            my_tasks.append(task_to_add)
            print(f"{task_to_add} added!")

def see_my_tasks():
    if not my_tasks:
        print("No tasks available! Add things to your to do list to get started!")
    else:
        for index, task in enumerate(my_tasks):
            print(index + 1, task)

def mark_items_complete():
    if not my_tasks:  
      print("No tasks available!")  
    else:
        task_to_mark = input("What task item would you like to mark as 'complete'? ")
        for task in my_tasks:
            if task not in my_tasks:
                print("Invalid item!")
            elif task_to_mark == task:
                print(task, "moved to completed tasks!")
                completed_tasks.append(task)
                my_tasks.remove(task)
        print("Here is your current to-do list:")
        for task in my_tasks:
            print(task)
        print("\nHere are your completed tasks:")
        for complete in completed_tasks:
            print(complete)
        

def deleteItem():
    item_to_remove = input('Which item would you like to remove from your to-do list? ')
    if item_to_remove not in my_tasks:
        print("That item does not exist.")
    try:
        my_tasks.remove(item_to_remove)
    except ValueError:
        print("Please enter the item you would like to remove by name!")
    else:
        print(my_tasks)
    finally:
        print("Your item has been removed!")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View current tasks")
        print("3. Mark task item complete")
        print("4. Remove item from list")
        print("5. Quit/Exit")
        choose_menu_option = int(input("\nWhat would you like to do? "))
        if choose_menu_option == 1:
            addTask()
        elif choose_menu_option == 2:
            see_my_tasks()
        elif choose_menu_option == 3:
            mark_items_complete()
        elif choose_menu_option == 4:
            deleteItem()
        elif choose_menu_option == 5:
            print("I hope you were productive today! Goodbye!")
            break

main_menu()