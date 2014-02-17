from socket import *
import sys
	
#if(len(sys.argv)!=2):
 #   print ("Please include server name")
  #  exit(1)
i=0
check=0
#string=str(sys.argv[1])
name="localhost" 
HOST = name
PORT = 16003    
ADDR = (HOST,PORT)
BUFSIZE = 4096
decrypt={}
for key, value in dic.iteritems():
	decrypt[value]=key
cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))
count=0
f=file("log.txt","w+")
while(count<10):
        s=""
	data = cli.recv(BUFSIZE)
	print (data)
	f.write(data+"\n")
	data=str(data)
	for letter in data:
		s=s+str((decrypt[letter]))
	print(s)
	f.write(s+"\n")
	count=count+1
cli.close()
f.close()
