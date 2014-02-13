from socket import *      #import the socket library
import os.path
import time


dic={
      	 'a':'.',
	     'b':'y',
	     'c':'r',
	     'd':'a',
	     'e':'!',
	     'f':'t',
	     'g':'h',
	     'h':'g',
	     'i':'?',
	     'j':'q',
	     'k':'o',
	     'l':'v',
	     'm':'p',
	     'n':'c',
	     'o':'x',
	     'p':'d',
	     'q':'s',
	     't':'k',
	     'r':'i',
	     's':'w',
	     'u':'z',
	     'v':' ',
	     'w':'l',
	     'x':'m',
	     'y':'u',
	     'z':'n',
	     '.':'e',
	     '!':'j',
	     '?':'f',
	     ' ':'b'};


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
f=open("messages.txt")
while(True): 
   # if(os.path.isfile("/tmp"+str(request)+)!=True):
    #        conn.send(" File Not Found".encode('utf-8'))
     #       continue
    text=f.readline()
    message=""
    for letter in text:
	        if(letter=='\n'):
		   break
		message=message+str((dic[letter]))
    conn.send(message.encode('utf-8'))
    request=request+1
    if(request==10):
	break
    time.sleep(5)
conn.close()
