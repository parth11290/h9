print("welcome to hamari dunia....aapka hamari dunia me sawagat hai")
while True:
    print() 
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6. sq.")
    print("7. cube")
    print("8. sq root")
    print("9. cube root")
    print("10. simple intrest")
    print("11. compound intrest")
    print()

    seva = int(input("Kripia , seva select kare : "))
    print()

    

    if seva in [1 ,2 ,3 ,4]:
        pehla = float(input("pelha no. dalo sa :"))
        doosra = float(input("Doosra no. bhi dalo sa :"))

    elif seva in[5]:
        num = float(input("no. :"))
        power = float(input("power :"))

    elif seva in [6, 7, 8, 9]:
        pintu = float(input("no. hajir ho :"))

    elif seva in [10, 11]:
        tinu = float(input("Principal kai hai sa :"))
        minu = float(input("rate bhi batao sa :"))
        cinu = float(input("Time bhi bata hi do sa ab :"))
        io=input("time is half yearly , quaterly or yearly")
    else:
        print("tu meri naukri se get outt")

        print()

    if seva == 1:
        print("jawab =",pehla + doosra)
        print()

    elif seva == 2:
        print("jawab =",pehla - doosra)
        print()

    elif seva == 3:
        print("jawab =",pehla * doosra)
        print()

    elif seva == 4:
         if doosra == 0:
            print("palhe phurasat me nikal")
         else:
             print("jawab =",pehla / doosra)
             print()

    elif seva == 5:
        print("jawab =",num ** power)
        print()
        
    elif seva == 6:
        print("jawab =",pintu ** 2)
        print()

    elif seva == 7:
        print("jawab =",pintu ** 3)
        print()

    elif seva == 8:
        print("jawab =",pintu ** 0.5)
        print()

    elif seva == 9:
        print("jawab =",pintu ** (1/3))
        print()

    elif seva == 10:
        if io =="half yearly":
            print("intrest =",(tinu * minu/2 * cinu*2)/100)
        elif io =="quaterly":
            print("intrest =",(tinu * minu/4 * cinu*4)/100)
        elif io =="yearly":
            print("intrest =",(tinu * minu * cinu)/100)    
        print()
    elif seva == 11:
        if io == "half yearly":
            print("amount =",tinu * (1 + (minu/2)/100) ** (2*cinu))
        elif io == "quaterly":
            print("amount =",tinu * (1 + (minu/4)/100) ** (4*cinu))
        elif io == "yearly":
             print("amount =",tinu * (1 + minu/100) ** cinu)
        print()

    else:
        print("kalti mar")
        exit()

    repet = input("or koi seva?  (ha/na) : ")
    if repet.lower() == "ha":
        continue
    else:
        print()
        print("hamare pas aane ke liye shukriya...or koi seva ho toh yaad jarur kariye ga")
        exit()

