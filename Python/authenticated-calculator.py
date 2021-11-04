import colorama
from colorama import Fore # coloring text
from getpass import getpass # hide input and echo

name = input("What is your name: ")
print("Hello %s" % (name,)) # print the value inserted into "name"

password = getpass("Please enter your password: \n")
passwd = ("toor" [::-1] + "123")

def is_acceptable_password(password):
    return len(password) > 6 # evaluates if the characters from the password value is more than 6
def simple_math_calculation(x, y, z):
    if x > 100:
        print(x, "is more than 100")
    elif x < 60:
        print(x, "is less than 60")

# print(is_acceptable_password(password)) 
print("\nThe password is acceptable! \nYour password length is:", len(password) ,"which is within the range (6-20)") if len(password) > 6 and len(password)  < 20 else print("\nThe password is not acceptable! \nYour password length is:", len(password)) # Short Hand If..Else

# print if the password is correct
print(Fore.GREEN + "The password is correct!\n" + Fore.WHITE) if password == passwd else print(Fore.RED + "The password is incorrect!\n" + Fore.WHITE)

if password == passwd: # if password is correct; ask for questions
    y = int(input("Insert value 1: "))
    z = int(input("Insert value 2: "))
    x = y*z
    simple_math_calculation(x, y, z)
else:
    print("Calculator can't start \nTry again later \n")



