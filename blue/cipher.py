import random
import copy

class Alphabetic:
	#list of the alphabet we are using
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
	#list of 100 monoalphabetic keys
	keyList=[]
	times = 0

	def __init__(self, MAPS):
		#global alphabet, keyList
		self.alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
		random.seed(10)
		self.keyList=[]
		self.times = MAPS #Number of times to map the cipher
		#this copies the alphabet and then shuffles it 100 times for 100 keys
		for x in xrange(0,100):
			thing = copy.deepcopy(self.alphabet)
			self.keyList.append(thing)
			random.shuffle(self.keyList[x])

	def encrypt(self, thing):
		#global alphabet, keyList, times
		message = str(thing)
		encrypted = ""
		t = 0
		#encrypts message polyalphabetically (doing it monoalphabetically just means you dont increment t)
		for letter in message:
			if(letter=='\n'):
			  continue
			encrypted+=(self.keyList[t][self.alphabet.index(letter)])
			t = (t + 1)%self.times
		print(encrypted)
		return encrypted

	def decrypt(self, thing):
		#global alphabet, keyList, times
		decrypted = ""
		t = 0
		for letter in thing:
			if(letter=='\n'):
			  continue
			decrypted+=self.alphabet[self.keyList[t].index(letter)]
			t = (t + 1)%self.times
			print (self.times)
		print(decrypted)
		return decrypted
