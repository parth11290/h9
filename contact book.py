import time
import os
def t():
    os.system("cls")

def r():
    input("Press enter to continue")

def s():
    i="CONTACT BOOK"
    print("*-" * 40)
    print(i.center(80))
    print("*-" * 40)

file = r"C:\Users\dell\Desktop\oo.py\contacts.txt"
def load():
    contacts={}
    try:
        with open(file,"r") as f:
            for line in f:
                n,nu=line.strip().split(",")
                contacts[n]=nu
    except:
        FileNotFoundError
        pass
    return contacts

def save(contacts):
    with open(file,"w")as f:
        for n,nu in contacts.items():
            f.write(f"{n},{nu}\n")
contacts=load()

def add():
    
    print()
    n=input("Enter contact name : ").strip()
    nu=input("enter number : ").strip()
    print()
    print("Added Successfully!! ")
    r()
    contacts[n]=nu
    save(contacts)

def view():
   
    print()
    if not contacts:
        print("No contacts found ")
        r()
    else:
        print("All contacts :")
        for n,nu in contacts.items():

            print(n,":",nu)
            r()

def search():
    
    print()
    n=input("Enter contact name to search : ").strip()
    if n in contacts:
        print(n,":",contacts[n] )
        r()
    else:
        print("Contact not found ")
        r()

def delet():
    
    print()
    n=input("Enter contact name : ").strip()
    if n in contacts:
        del contacts[n]
        save(contacts)
        print("Deleted Successfully!! ")
        r()

    else:
        print("contact not found ")
        r()
def exi():
    print("ThankYou!!")
    time.sleep(1)
    exit()
    

def yu():
    load()
    t()
    i="Welcome to Contact book!!"
    e="*menu"
    print("*-" * 40)
    print(i.center(80))
    print("*-" * 40)
    print(e.center(80))
    
    print()
    print("1. Add contacts".center(80))
    print("2. view contacts".center(80))
    print("3. search contacts".center(80))
    print("4. Delet contacts".center(80))
    print("5. Exit".center(80))
    print()
    o=input("What You have to doo??  ").strip()
    t()
    s()
    print()
    if o == "1":
        add()
    if o == "2":
        view()
    if o == "3":
        search()
    if o == "4":
        delet()
    if o == "5":
        exit()

        

    t()
    print()
    print("1. Back to main menu")
    print("2. Exit")
    print()
    u=input("Which one??  ").strip()
    if u == "1":
        yu()

    else:
        exi()
    


yu()