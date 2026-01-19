print("welcome to crazy calculator!!")
print()

while True:
    a = float(input(" enter your no. :"))
    b = float(input("enter 2nd no. :"))
    num1 = b
    num = a
    print()
    print("choose operation,")
    opera = input("+ , - , x , / : ")
    print()
    if opera == "+":
        result = a + b
        print("answer is", result)
    elif opera == "-":
            result = a - b
            print("answer is ", result)
    elif opera == "x":
        result = a * b
        print("your ans is : ", result)
    elif opera == "/":
        result = a / b
        print("ans :",result)
    else:
        print("invalid operation")

        print()

    abc = input("would you like to do more calculations (yes/no) : ")
    if abc.lower() != "yes":
            break

print()
print("thanks for using calculator !")
exit()
