from socket import *
import sys

from homo import Homophonic
from polygram import Polygram
from cipher import Alphabetic

name="localhost" #Change to client for test on deterlab
HOST = name
PORT = 16008
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))

#Receive type of cipher to use and any additional info
data = cli.recv(BUFSIZE)
dataSplit = str(data).split()

if(dataSplit[0] == "a"):
	crypt = Alphabetic(1)

elif(dataSplit[0] == "b"):
	crypt = Alphabetic(4)
	
elif(dataSplit[0] == "c"):
	crypt = Homophonic()
	
elif(dataSplit[0] == "d"):
	crypt = Polygram()

#Begin receiving file, decrypting, and logging
f = file("log.txt","w+")

while(True):
	data = cli.recv(BUFSIZE) #Receive the message from server

	if(data == "bac.,!? "): #Checks for end of messages, if so break out of while
		break

	#f.write(data+"\n")
	data = str(data)
	number=data[0:2]
	data = data[2:] #Strip order number from string. Discard it for now?
	s = crypt.decrypt(data) #Decrypt the message
	
	#Strip spaces from end of message in case of polygram
	if(dataSplit[0] == "d"):
		s.strip()	

	#Write decrypted message to log.txt
	f.write(str(number)+". "+s + "\n")

cli.close()
f.close()
