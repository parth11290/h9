import os
import time
import string
def ji():
    os.system("cls")

def pause():
    input("press enter key to continue")
title = "unit converter"
def hedder(title):
    print("-" * 70)
    print(title.center(70))
    print("-" * 70)
    

def main_menu():
    oop = "==*menu*=="
    print(oop.center(19))
    print("1. length converter ")
    print("2. temperature converter")
    print("3. rupees to dollar")
    print("4. exit")

    print()
    io = input("select operation : ")    
    print()
    pause()
    ji()
    print()
    if io == "1":
        le()
    elif io == "2":
        te()
    elif io == "3":
        ru()
    else:
        print("thanks for using unit converter")
        time.sleep(3)
        exit()
print()
def le():
    print()
    opp = "==*Length Converter*=="
    print(opp.center(22))
    print()    
    print("1. meter to centimeter")
    print("2. centimeter to meter")
    print("3. meter to kelometer")
    print("4. kelometer to meter")
    print()
    ppo = input("select operation : ")
    print()
    pause()
    ji()
    print()
    if ppo == "1":
        d = float(input("meter value : "))
        print("centimeter : ",d * 100)

    if ppo == "2":
        d = float(input("cm value : "))
        print("meter : ", d / 100)
    if ppo == "3":
        d = float(input("meter value : "))
        print("meter : ",d * 1000)
    if ppo=="4":
        d = float(input("km value : "))
        print("meter : ",d / 1000)

print()
def te():
        print()
        opp = "==*temperature Converter*=="
        print(opp.center(22))
        print()    
        print("1. celcious to feharanite")
        print("2. feharanite to celcious")
        print("3. celcious to kelvin")
        print("4. kelvin to celcious")
        print("5. feharanite to kelvin")
        print("6. kelvin to feharanite")

        print()
        ppo = input("select operation : ")
        print()
        pause()
        ji()
        print()
        if ppo == "1":
            d = float(input("celcious : "))
            print("feharanite : ",(d * 9/5)+32)
        if ppo == "2":
                d = float(input("feharanite value : "))
                print("celcious : ", (d-32)*5/9)
        if ppo == "3":
            d = float(input("celcious : "))
            print("kelvin : ",d + 273.15)
        if ppo=="4":
            d = float(input("kelvin : "))
            print("celcious : ",d - 273.15)
        if ppo=="5":
            d=float(input("feharanite : "))
            print("kelvin : ",d-32*5/9+273.15)
        if ppo=="6":
            d=float(input("Kelvin : "))
            print("farahnite : ",d-273.15*9/5+32)

print()

def ru():
    print()
    op="Rupees to Dollar"
    print(op.center(22))
    d=float(input("Enter amount : "))
    print(d/90.38," : dollars")
    
hedder(title)
main_menu()

print()
o=input("YOU WANT TO DO MORE?? (yes/no)")
if o =="yes":
    main_menu()
else:
    time.sleep(1)
    exit()
    

























