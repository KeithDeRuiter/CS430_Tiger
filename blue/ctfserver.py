from socket import *      #import the socket library
import os.path
import time

HOST = ""   #we are the host
PORT = 16003    #arbitrary port not currently in use
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
while(true):
	#Choose cipher type
	ciphertype = input("Select cipher letter choice: a) monoalphabetic, b) polyalphabetic, c) homophonic, d) polygram :")
	if(ciphertype == "a"):
		choice = "a"
		conn.send(choice)
		crypt = #FILL IN THIS WITH CLASS NAME
		break

	else if(ciphertype == "b"):
		maplen = input("How many maps to use: ")
		choice = "b " + maplen
		conn.send(choice)
		crypt = #FILL IN THIS WITH CLASS NAME
		break

	else if(ciphertype == "c"):
		choice = "c"
		conn.send(choice)
		crypt = #FILL IN THIS WITH CLASS NAME
		break

	else if(ciphertype == "d"):
		blocklen = input("How long of a block: ")
		choice = "d " + blocklen
		conn.send(choice)
		crypt = Polygram(blocklen)
		break

	else
		print("Not a valid choice. ")

count = 0

with open("messages.txt") as f: #Opens file and goes through every line. Appends not encrypted count to keep track.
    for line in f:
    	count += 1
		message = crypt.encrypt(str(line))
		message = count + message
		conn.send(message.encode('utf-8'))
		time.sleep(60)

#Tells receiver that all messages sent?
done = "abcdefghijklmnopqrstuvwxyz.,!? " #Random message to send
conn.send(done)

conn.close()
