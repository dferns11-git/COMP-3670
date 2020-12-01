#!/usr/bin/env python
#Importing scapy library
from scapy.all import *

#This function prints the IP address of the source 
#This function will print the connected devices on the networks IP address


def printing(pkt):
    if IP in pkt:
        ipsrc=pkt[IP].src
        ipdst=pkt[IP].dst
    if TCP in pkt:
        tcpsport=pkt[TCP].sport
        tcpdport=pkt[TCP].dport

        print (" IP source " + str(ipsrc) + " TCP Source Port " + str(tcpsport))
        print (" IP destination " + str(ipdst) + " TCP Destination Port" + str(tcpdport))

  
    if ( ( pkt[IP].src == "192.168.0.1") or ( pkt[IP].dst == "192.168.0.1") ):
        print("!")

sniff(filter="ip",prn=printing)
sniff(filter="ip and host 192.168.0.1",prn=printing)