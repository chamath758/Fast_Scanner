#!/usr/bin/python
from ipaddress import ip_address, ip_network
from numbers import Number
import socket
import os
import nmap3
import pyfiglet
from tabulate import tabulate
from datetime import datetime
import sys


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(0.5)
ascii_banner = pyfiglet.figlet_format("!!! Fast_Sanner !!!")
print(ascii_banner)
print("\n****************************************************************")
print("\n*              Copyright of Black_hat___, 2022                 *")
print("\n****************************************************************") 
if os.geteuid() != 0:
    exit("You need to have root privileges to run FAST SCANNER.\nPlease try again, this time using 'sudo'. Exiting.")

data = [["Port Scanner"], 
        ["Os Scanner"], 
        ["DNS Scanner"], 
        ["Fin_Scanner"],
        ["Version Scanner"],
        ["idle_Scanner"],
        ["Ping_Scanner(ICMP)"], 
        ["Syn_Scanner"], 
        ["TCP_Scanner"],
        ["UDP_Scanner"],
        ["EXIT"]]
  
#define header names
col_names = ["Features"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

#banner_time and date
print("_" * 100)
print("Scanning started at: " + str(datetime.now()))
print("_" * 100)


#Port Scanner
def portScanner(port1,port2): 
    print("_"*100)
    for x in range(port1,port2):
        y=x
        
        results=s.connect_ex((host, y))
        if results==0:
            print("[*] Port {} is open".format(y))
        else:
            print("[*] Port {} is closed".format(y))
        s.close()
    print("_"*100)
      
#Os Scanner 

def Os_Scanner(host):
    nmap = nmap3.Nmap()
    os_results = nmap.nmap_os_detection(host)
    print("_"*100)
    print(os_results)
    print("_"*100)
    
##DNS Scanner
def Dns_Scanner(host):
    nmap = nmap3.Nmap()
    results = nmap.nmap_dns_brute_script(host)
    print("_"*100)
    print(results)
    print("_"*100)

##Fin Scaner
def Fin_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_fin_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)
##Version Detector
def Version(host):
    nmap = nmap3.Nmap()
    version_result = nmap.nmap_version_detection(host)
    print("_"*100)
    print(version_result)
    print("_"*100)

##idle_scan
def idle_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_idle_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)

##ping_scan
def ping_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_ping_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)

##syn_scan
def syn_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_syn_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)

##tcp_scan
def TCP_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_tcp_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)

##UDP_scan
def UDP_Scanner(host):
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_udp_scan(host)
    print("_"*100)
    print(result)
    print("_"*100)



#Selection numbers
while (True):
    Num1=int(input("Enter Selection Number: "))
    if(Num1>11):
        print("Please Enter Correct Number for Selection")
        exit()
    elif Num1==0:
        host= input("Enter ip address: ")
        port1=int(input("Enter port range between 1,65535: "))
        port2=int(input("Enter port range between 1,65535: "))
        portScanner(port1,port2)
        continue
    elif Num1==1:
        host= input("Enter ip address: ")
        Os_Scanner(host)
        continue
    elif Num1 == 2:
        host= input("Enter Domain Name: ")
        Dns_Scanner(host)
        continue
    elif Num1==3:
        host= input("Enter ip address: ")
        Fin_Scanner(host)
        continue
    elif Num1==4:
        host= input("Enter ip address: ")
        Version(host)
        continue
    elif Num1==5:
        host= input("Enter ip address: ")
        idle_Scanner(host)
        continue
    elif Num1==6:
        host= input("Enter ip address: ")
        ping_Scanner(host)
        continue
    elif Num1==7:
        host= input("Enter ip address: ")
        syn_Scanner(host)
        continue
    elif Num1==8:
        host= input("Enter ip address: ")
        TCP_Scanner(host)
        continue
    elif Num1==9:
        host= input("Enter ip address: ")
        UDP_Scanner(host)
        continue

    else:
        if (Num1==10):

            ascii_banner2 = pyfiglet.figlet_format("Have a Nice Day!!!")
            print(ascii_banner2)
            print("_"*100)
            os.system("python main.py")

    
            


   









 
    

