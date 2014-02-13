from socket import *
import sys

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
