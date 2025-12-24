import random
import string

def o():
    print("welcome to password generater")
print()
ji = int(input("Enter your password's length : "))
print()
oi = string.ascii_lowercase +string.ascii_uppercase+ string.digits +string.hexdigits
ki = "".join(random.choice(oi)for i in range(ji))
print("your paassword : ",ki)
print()
print("thank you")

print()
io=input("You wanna do it again??")
if io== "yes":
    o()

else:
    exit()