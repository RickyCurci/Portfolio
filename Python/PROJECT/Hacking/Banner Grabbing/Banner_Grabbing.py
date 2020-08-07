import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for host in range(100, 150):
	ports = open("porte.txt", "r")
	vulnbanners = open('vulnbanners.txt','r')
	for port in ports:
		try:
			socket.connect(( str(sys.argv[1]+'.'+str(host)), int(port) ))
			print("Connessione in corso "+str(sys.argv[1]+'.'+str(host))+" nella porta "+str(port))
			socket.settimeout(1)
			banner = socket.recv(1024)
			for vulnbanner in vulnbanners:
				if banner.strip() in vulnbanner.strip():
					print("ok ho trovato qualcosa! "+banner)
					print("Host "+str(sys.argv[1]+'.'+str(host)))
					print("Port "+str(port))
		except:
			print("errore di connessione ")
