#! /usr/bin/python
from logging import getLogger,ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from scapy.all import*
#Importing scapy library
import sys
#Importing date and time library to use to print time and date stamp
from datetime import datetime
from time import strftime

#We are acquring input from the user to enter the range of ports they wish to scan
#Should it pass the requirement it will perform the scan else it will give you an error saying 
#Invalid range of port and exit the program
try:
        target = input("[*] Enter Target IP address: ")
        min_port = input("[*] Enter Minumum Port Number: ")
        max_port = input("[*] Enter Maximum Port Number: ")
        try:
                if int(min_port) >= 0 and int(max_port) >=0 and int (max_port) >= int(min_port):
                    pass
                else:
                    print ("\n[!] Invalid Range of Ports")
                    print ("[!] Exiting...")
                    sys.exit(1)
        except Exception:
            print ("\n[!] Invalid Range of Ports")
            print ("[!] Exiting...")
except KeyboardInterrupt:
            print ("\n[*] User Requested Shutdown...")
            print ("[*] Exiting...")
            sys.exit(1)

#This part assigns the values the that was taken as input.
#start_clock will be the timestamp of when the scan is requested.
#The flags of the SYNACK and RSTACK are set to be referenced later.
ports=range(int(min_port),int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14




#This part checks if the IP address provided is up and running that is the reason for it being pinged.
#It will throw and execption incase the target is not resolved.
def checkhost(ip):
            conf.verb = 0
            try: 
                    ping = sr1(IP(dst = ip)/ICMP())
                    print ("\n[*] Target is up, Beginning Scan....")
            except Exception:
                    print ("\n[!] couldn't Resolve Target")
                    print ("[!] Exiting...")
                    sys.exit(1)
                    
#After the IP address is confirmed it scans the port 
#Returns a boolean value based on SYNACK                     
def scanport (port):
   
    srcport = RandShort()
    conf.verb = 0
    synackpkt = sr1(IP(dst = target)/TCP (sport = srcport, dport = port,flags ="S"))
    pktflags = synackpkt.getlayer (TCP).flags
    if pktflags == SYNACK:
       return True
    else:
       return False
    RSTpkt = IP( dst = target)/TCP (sport = srcport, dport = port,flags="R")
    send(RSTpkt)

#Prints the status of the port which lets the user know when the scanner was initiated

checkhost(target)
print ("[*] SCANNING STARTED AT " + strftime("%H : %M : %S") + "!\n")

for port in ports:
    status = scanport(port)
    if status == True:
        print ("PORT " + str(port) + ":open")

#Prints the time the scanner is done executing and prints the time taken for the entire scan to be completed
        stop_clock = datetime.now()
        total_time = stop_clock - start_clock
print("\n[*] SCANNING FINISHED !")
print("[*] TOTAL SCAN DURATION:" + str(total_time))