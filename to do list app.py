import time
import os
file = r"c:\Users\dell\Desktop\tasks.txt"
def load():
    try:
        task=[]
        with open(file,"r")as f:
            for line in f:
                task.append(line.strip())
    except FileNotFoundError:
        pass
    return task
def save(tasks):
    with open(file,"w")as f:
        for i in tasks:
            f.write(i+"\n")
tasks=load()
def add():
    i=input("Enter task to be added :")
    tasks.append(i)
    save(tasks)
def show():
    if not tasks:
        print("No tasks found ")
    else:
        print("All tasks :")
        for e, task in enumerate(tasks, start=1):
            print(e,":",task)
def delete():
    show()
    if not tasks:
        return
    try:
        i=int(input("Enter task number to be deleted :"))
        if 1<=i<=len(tasks):
            removed_task=tasks.pop(i-1)
            print()
            print(f'Task "{removed_task}" has been deleted.')
            save(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def menu():
    os.system("cls")
    print("*"*20)
    print("TO DO LIST".center(20))
    print("*"*20)
    print()
    print("1.Add task")
    print("2.Show tasks")
    print("3.delet tasks")
    print()
    i=input("WHICH ONE??")
    print()
    os.system("cls")
    if i=="1":
        add()
    elif i == "2":
        show()
    elif i=="3":
        delete()
    else:
        print("Invalid")
        return
def op():
    os.system("cls")
    print()
    print("1. go back to mein menu")
    print("2. Exit")
    o=input("WHICH ONE??")
    try:
                    if o=="1":
                            menu()
                    elif o=="2":
                     print("THANKYOU")
                    time.sleep(1)
                    exit()
    except ValueError:
     pass
    return 
    print("THANKYOU")
menu()
print()
print("THANKYOU")
op()