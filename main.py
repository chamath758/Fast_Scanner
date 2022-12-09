#!/usr/bin/python
import os
import __pycache__
import pyfiglet
from tabulate import tabulate
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Fast_Vulnerability_Sanner")
print(ascii_banner)

if os.geteuid() != 0:
    exit("You need to have root privileges to run FAST SCANNER.\nPlease try again, this time using 'sudo'. Exiting.")


data = [["Network Vulnerability Scanner"], 
        ["Cross Site Scripting Scanner"], 
        ["Fast_WordPress_Sanner"],
        ["Password_Generator_And_Cyber_Adveseries"]
       

       ]
  
#define header names
col_names = ["Features"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

#banner_time and date
print("_" * 100)
print("Scanning started at: " + str(datetime.now()))
print("_" * 100)

X=input("Enter Number: ")
if int(X)==0:
    os.system("python PortScanner.py")
elif int(X)==1:
    os.system("python xss_Caller.py")
elif int(X)==2:
    os.system("python WP_Scanner/WP_Scanner.py")
elif int(X)==3:
    os.system("python Passwd.py")



    

    
        

   
    
