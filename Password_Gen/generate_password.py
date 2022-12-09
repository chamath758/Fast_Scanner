import secrets
import string
import pyfiglet
from tabulate import tabulate
from datetime import datetime
import os

ascii_banner = pyfiglet.figlet_format("Fast_Secure_Password_Generator")
print(ascii_banner)


def password_gen(password_length):

    characters = string.ascii_letters + string.digits

    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))

    return secure_password

def main():

    user_password_length = int(input("Input number of digits for password: "))

    print("Password Generated: ", password_gen(user_password_length))

    X=input("If You want go main menu ?(Y/N): ")
    if(X=="Y"):
        os.system("python main.py")
    elif(X=="N"):
         os.system("python Passwd.py")
    
main()


