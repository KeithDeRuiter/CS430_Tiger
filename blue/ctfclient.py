from socket import *
import sys

import polygram
import homo
import cipher

name="localhost" #Change to client for test on deterlab
HOST = name
PORT = 16003
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))

#Receive type of cipher to use and any additional info
data = cli.recv(BUFSIZE)
dataSplit = data.split()
if(dataSplit[0] == "a")
	crypt = Alphabetic(1)

else if(dataSplit[0] == "b")
	crypt = Alphabetic(dataSplit[1])
	
else if(dataSplit[0] == "c")
	crypt = Homophonic()
	
else if(dataSplit[0] == "d")
	crypt = Polygram(dataSplit[1])

#Begin receiving file, decrypting, and logging
f = file("log.txt","w+")

while(True):
	data = cli.recv(BUFSIZE) #Receive the message from server

	if(data == "bac.,!? ") #Checks for end of messages, if so break out of while
		break

	#f.write(data+"\n")
	data = str(data)
	data = data[1:] #Strip order number from string. Discard it for now?
	s = crypt.decrypt(data) #Decrypt the message
	
	#Strip spaces from end of message in case of polygram
	if(dataSplit[0] == "d")
		s.strip()	

	#Write decrypted message to log.txt
	f.write(s + "\n")

cli.close()
f.close()
