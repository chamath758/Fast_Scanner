#!/usr/bin/python
import os
import __pycache__
import pyfiglet
from tabulate import tabulate
from datetime import datetime





ascii_banner = pyfiglet.figlet_format("Fast_Vulnerability_XSS_Sanner")
print(ascii_banner)

data = [["Load custom payload directly"], 
        ["Set cookie"], 
        ["payload Generator"],
        ["Main Menu"]
       ]
  
#define header names
col_names = ["Features"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))
    
Y=int(input("Enter Choosen Number:"))
if int(Y)==0:
    opt2=input("Enter Website Domain: ")
    opt4="--payload-level"
    opt3="-u"
    opt11="7"
    os.system("python Fast_XSS/pwnxss.py "+" "+opt3+" "+opt2+" "+opt4+" "+opt11)
    print(" ")
    
elif int(Y)==1:
    opt2=input("Enter Website Domain: ")
    opt9=input("Enter Cookie Value(ex-{'ID':'1094200543'}):")
    opt3="-u"
    opt5="--cookie"
    os.system("python Fast_XSS/pwnxss.py "+" "+opt3+" "+opt2+" "+opt5+" "+opt9)
    print(" ")
elif int(Y)==2:
    opt2=input("Enter Website Domain: ")
    opt3="-u"
    opt6="--payload-level"
    opt12="6"
    os.system("python Fast_XSS/pwnxss.py "+" "+opt3+" "+opt2+" "+opt6+" "+opt12)
elif int(Y)==3:
    os.system("python main.py")