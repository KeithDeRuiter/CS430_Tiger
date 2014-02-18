from socket import *      #import the socket library
import os.path
import time

from homo import Homophonic
from polygram import Polygram
from cipher import Alphabetic

HOST = ""   #we are the host
PORT = 16005   #arbitrary port not currently in use
ADDR = (HOST,PORT)    #we need a tuple for the address
BUFSIZE = 4096    #reasonably sized buffer for data
## now we create a new socket object (serv)
## see the python docs for more information on the socket types/flags

serv = socket( AF_INET,SOCK_STREAM)    

##bind our socket to the address
serv.bind((ADDR))    #the double parens are to create a tuple with one element

serv.listen(5)    #5 is the maximum number of queued connections we'll allow
print ("listening...")
request=0
conn,addr = serv.accept() #accept the connection
print ("...connected!")


#Setup which cipher type and additional info needed
while(True):
	#Choose cipher type
	ciphertype = raw_input("Select cipher letter choice: a) monoalphabetic, b) polyalphabetic, c) homophonic, d) polygram : ")
	print(ciphertype)
	if(ciphertype == "a"):
		choice = "a"
		conn.send(choice)
		crypt = Alphabetic(1)
		break

	elif(ciphertype == "b"):
		maplen = input("How many maps to use: ")
		choice = "b " + str(maplen)
		conn.send(choice)
		crypt = Alphabetic(maplen)
		break

	elif(ciphertype == "c"):
		choice = "c"
		conn.send(choice)
		crypt = Homophonic()
		break

	elif(ciphertype == "d"):
		blocklen = input("How long of a block: ")
		choice = "d " + str(blocklen)
		conn.send(choice)
		crypt = Polygram(blocklen)
		break

	else:
		print("Not a valid choice. ")

count = 0

with open("messages.txt") as f: #Opens file and goes through every line. Appends not encrypted count to keep track.
	for line in f:
		if(str(line)=="\n"):
		  continue
		count=int(count)
		count += 1
		message = str(crypt.encrypt(str(line)))
		if(count<10):
		  count="0"+str(count)
		message = str(count) + (message)
		conn.send(message.encode('utf-8'))
		time.sleep(5)

#Tells receiver that all messages sent?
done = "bac.,!? " #Random message to send
conn.send(done)

conn.close()
