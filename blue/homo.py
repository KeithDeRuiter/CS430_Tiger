import random
import copy

class Homophonic:
	#list of the alphabet + punctuation for decrypting
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
	homophonic = []

	def __init__(self):
		self.alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
		self.homophonic=[]
		#list used to encrypt and decrypt, each character maps to 100 different numbers
		self.homophonic = list(range(1000, 10000))
		random.seed(10)
		random.shuffle(self.homophonic)

	def encrypt(self, thing):
		count = 0
		message = ""
		#encrypts the message by converting each character to some 4 digit number
		for letter in thing:
		        if(letter=='\n'):
			  continue
			message = message + str(self.homophonic[self.alphabet.index(letter)*100+count])
			count = count+1
		print(message)
		return message

	def decrypt(self, thing):
		message = ""
		#decrypts by seeing what 4 digit number maps to what character
		for x in xrange(0, len(thing)/4): 
			temp = thing[x*4:x*4+4]	
			message = message + self.alphabet[(self.homophonic.index(int(temp))/100)]
		print(str(message))
		return str(message)
