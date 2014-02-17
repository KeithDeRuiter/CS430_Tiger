from socket import *
import sys

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
	crypt = #FILL IN THIS WITH CLASS NAME

else if(dataSplit[0] == "b")
	crypt = #FILL IN THIS WITH CLASS NAME
	
else if(dataSplit[0] == "c")
	crypt = #FILL IN THIS WITH CLASS NAME
	
else if(dataSplit[0] == "d")
	crypt = Polygram(dataSplit[1])

#Begin receiving file, decrypting, and logging
f = file("log.txt","w+")

while(True):
	data = cli.recv(BUFSIZE) #Receive the message from server

	if(data == "abcdefghijklmnopqrstuvwxyz.,!? ") #Checks for end of messages, if so break out of while
		break

	#f.write(data+"\n")
	data = str(data)
	data = data[1:] #Strip order number from string. Discard it for now?
	s = crypt.decrypt(data) #Decrypt the message
	f.write(s+"\n") #Write decrypted message to log.txt

cli.close()
f.close()
