import random
print("aao sath time pass karte hai....chalo guessing game khelte hai")
print()
print("select kar")
print("1. easy ")
print("2. normal")
print("3. hard")
print()
choi = int(input("konsa level?? : "))
print()
score = 0
print()
if choi ==1:
      limit=20
elif choi ==2:
      limit=50
elif choi ==3:
      limit=100
num=random.randint(1,limit)
def ip():
    score = 0
    oi = int(input("Enter Your Guess : "))
    print()
    if oi > num:
        print("so ahead...lagta hai bought door kr soachte ho")
        print()
    elif oi < num:
        print("thoda kam hai....thoda bada num tha")
        print()

    else:
        print("yupp,... you are correct")
        print()
        score += 1
        print("score =",score)
        print()
        exit()


if choi == 1:
      print("4 life")
      limit = 20
      print(limit," limit")
      print("score =",score)
      print()
      ip()
      ip()
      ip()
      ip()
      print("number was ",num)
elif choi == 2:
        print("3 life")
        limit = 50
        print(limit," limit")
        print("score =",score)
        print()
        ip()
        ip()
        ip()
        print("number was ",num)
elif choi == 3:
        print("2 life")
        limit = 100
        print(limit," limit")
        print("score =",score)
        print()
        ip()
        ip()
        print("number was ",num)
else:
        exit()
        print()
        
print("thankyouu!!")
exit()
       
       
       
        

        

    
        
    
    

            
        
        
        
  
