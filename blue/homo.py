import random
import copy
#list of the alphabet + punctuation for decrypting
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
#message to be encrypted
thing="aabccdeefgghiijkklmmnoopqqrsstuuvwwxyyz  .!!?"
#list used to encrypt and decrypt, each character maps to 100 different numbers
homophonic=list(range(1000,10000))
message=""
count=0
random.seed(10)
random.shuffle(homophonic)
#encrypts the message by converting each character to some 4 digit number
for letter in thing:
	message=message+str(homophonic[alphabet.index(letter)*100+count])
	count=count+1
print(message)
message2=""
#decrypts by seeing what 4 digit number maps to what character
for x in xrange(0,len(message)/4):
	temp=message[x*4:x*4+4]	
        message2=message2+alphabet[(thing2.index(int(temp))/100)]
print(message2)
