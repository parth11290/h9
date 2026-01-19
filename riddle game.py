import os
import time
def u():
    os.system("cls")
def w():
      input("Press enter to continue")
def i():
      print()
u()
print()
def g1():
        u()
        print("good choise!")
        print("Rules")
        print("Only 2 life will be given")
        print("You have to solve the riddles  ")
        print("Their will be 3 riddles given ")
        print("if solve all of them in 1st try")
        print("You will win and if you can't solve you will out")
        i()
        w()
        u()   
def g2():
    u()
    print("good choise!")
    print("Rules")
    print("Only single life will be given")
    print("You have to solve the riddles  ")
    print("Their will be 5 riddles given ")
    print("if solve all of them in 1st try")
    print("You will win and if you can't solve you will out")
    i()
    w()
    u()
def g22():
    print("1st riddle")
    print("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
    o=input("")
    if o=="map":
             print("Good..you are correct")
             True
    i()
    w()
    u()
    print("2nd.What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?")
    p=input("")
    if p=="r":
             print("Good..you are correct")
             True
    i()
    w()
    u()
    print("3rd..I have keys, but no locks , i have space, but no rooms. You can enter, but you can’t go outside. What am I?")
    t=input("")
    if t=="keyboard":
             print("Good..you are correct")
             True      
    i()
    w()
    u()
    print("4th..What has to be broken before you can use it?")
    d=input("")
    if d=="egg":
                   print("Good..you are correct")
                   True
    i()
    w()
    u()
    print("5th..This belongs to you, but everyone else uses it. What is it?")
    g=input("")
    if t=="keyboard" and p=="r" and o=="map" and d=="egg" and g=="name":
           print("Congratulations...you won")
    else:
            print("you are wrong and out of game buddy...better luck next time")
            i()
            w()
            u()
def ho():
      op=input("Do you want to play again (yes/no): ")
      if op=="yes":
            u()
            uio()
            goi()
      else:
            print("Thanks for playing..see you next time!!")
            time.sleep(2)
            exit()
def g11():   
         print("1st riddle")
         print("What gets smaller every time it takes a bath?")
         a=input("")
         if a=="soap":
              print("Good..you are correct")
def g12():
         print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
         p=input("")
         if p=="shirt":
                    print("Good..you are correct")
def g13():
         print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
         o=input("")
         if o=="SWIMS" :
                          print("You won buddy!!...congratulation!!")
def uio():
      print("so,welcome to our interesting game buddy!!")
      print()
      print("Their are modes  in this game")
      print("1. easy")
      print("2. hard")
      print()
def goi():
      poi=input("Select your mode (1 or 2): ")
      if poi=="1":
            g1()
            if g11():
                   g12()
                   if g12():
                          g13()
            else:
                   u()
                   print("you are wrong buddy...")
                   print()
                   print("You have 1 life left for next riddle")
                   print()
                   print("What gets smaller every time it takes a bath?")
                   a=input("")
                   if a=="soap":
                     print("Good..you are correct")
                     True
                   else:
                      print("you are wrong buddy...")
                      i()
                      w()
                      u()
                      ho()
                   u()
                   print("2nd..I have a neck, but no head. I have two arms, but no hands. What am I?")
                   p=input("")
                   if p=="shirt":
                        print("Good..you are correct")
                        True
                   else:
                        print("you are wrong buddy...")
                        i()
                        w()
                        u()
                        ho()
                   u()
                   print("3rd..What five-letter word typed in all capital letters can be read the same upside down?")
                   o=input("")
                   if o=="SWIMS" :
                          print("You won buddy!!...congratulation!!")
                   else:
                          print("you are wrong buddy...")
                          i()
                          w()
                          u()
                          ho()
            i()
            w()
            u()
            ho()
      elif poi=="2":
            g2()
            g22()
uio()
goi()
