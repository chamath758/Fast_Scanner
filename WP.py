#!/usr/bin/python
import os
import __pycache__
import pyfiglet
from tabulate import tabulate
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Fast_WordPress_Sanner")
print(ascii_banner)

data = [["Fast_WordPress_Scanner"], 
        ["Main_Menu"] 
       
       ]
  
#define header names
col_names = ["Features"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

#banner_time and date
print("_" * 100)
print("Scanning started at: " + str(datetime.now()))
print("_" * 100)

Y=int(input("Enter Choosen Number:"))
if int(Y)==0:
    os.system("python WP_Scanner/WP_Scanner.py")
elif int(Y)==1:
    os.system("python main.py")
    print("_" * 100)

