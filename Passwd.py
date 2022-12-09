#!/usr/bin/python
import os
import __pycache__
import pyfiglet
from tabulate import tabulate
from datetime import datetime





ascii_banner = pyfiglet.figlet_format("Password_Generator_And_Cyber_Adveseries")
print(ascii_banner)

data = [["Password_Generator"],  
        ["Latest_Adveseries"],
        ["CVE_LIST"],
        ["Main Menu"]
       ]
  
#define header names
col_names = ["Features"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

Y=int(input("Enter Choosen Number:"))
if int(Y)==0:
    os.system("python Password_Gen/generate_password.py")
elif int(Y)==1:
    os.system("python CyberSec_News/cybersecurity_news.py")
elif int(Y)==2:
    os.system("python CVE_LIST/cve_list.py")
elif int(Y)==3:
    os.system("python main.py")

