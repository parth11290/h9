import time
import os
import time
import string
import random
def u():
    os.system("cls")
def w():
      input("Press enter to continue")
def i():
      print()
u()
print()


def t():
      print("so,welcome to our interesting game buddy!!")
      print()
      print("Their are modes  in this game")
      print("1. easy")
      print("2. hard")
      print()
    
      i=input("Which Option :")

    
    

def g1():
        u()
        print("good choise!")
        print("Rules")
        print("Only single life will be given")
        print("You have to solve the riddles  ")
        print("Their will be 3 riddles given ")
        print("if solve all of them in 1st try")
        print("You will win and if you can't solve you will out")
        i()
        w()
        u()
        print("1st riddle")
        print("What gets smaller every time it takes a bath?")
        o=input("")
        if o == "soap":
              print("you are correct!!")
              w()
              u()
              print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
              p=input("")
              if p=="shirt":
                    print("again you are right!!")
                    w()
                    u()
                    print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
                    o=input("")
                    if o=="SWIMS":
                          print("You won buddy!!...congratulation!!")
        else:
              print("you are wrong buddy...better luck nxt time")
              time.sleep(2)
              exit()


t()
g1()








