import random
import copy

class Homophonic:
	#list of the alphabet + punctuation for decrypting
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
	homophonic = []

	def __init__(self):
		#global homophonic
		self.alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
		self.homophonic=[]
		#list used to encrypt and decrypt, each character maps to 100 different numbers
		self.homophonic = list(range(1000, 10000))
		random.seed(10)
		random.shuffle(self.homophonic)

	def encrypt(self, thing):
		#global alphabet, homophonic
		count = 0
		message = ""
		#encrypts the message by converting each character to some 4 digit number
		for letter in thing:
			message = message + str(self.homophonic[self.alphabet.index(letter)*100+count])
			count = count+1
		return message

	def decrypt(self, thing):
		#global alphabet
		message = ""
		#decrypts by seeing what 4 digit number maps to what character
		for x in xrange(0, len(message)/4):
			temp = thing[x*4:x*4+4]	
			message = message + self.alphabet[(thing.index(int(temp))/100)]
		return message
