import random
import copy

class Alphabetic:
	#list of the alphabet we are using
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
	#list of 100 monoalphabetic keys
	keyList=[]
	times = 1

	def __init__(self, MAPS):
		global alphabet, keyList, 
		random.seed(10)
		times = MAPS #Number of times to map the cipher
		#this copies the alphabet and then shuffles it 100 times for 100 keys
		for x in xrange(0,100):
			thing = copy.deepcopy(alphabet)
			keyList.append(thing)
			random.shuffle(keyList[x])

	def encrypt(self, thing):
		global alphabet, keyList, times
		message = str(thing)
		encrypted = ""
		t = 0
		#encrypts message polyalphabetically (doing it monoalphabetically just means you dont increment t)
		for letter in message:
		  encrypted+=(keyList[t][alphabet.index(letter)])
		  t = t + 1
		print(encrypted)

	def decrypt(self, thing):
		global alphabet, keyList, times
		decrypted = ""
		t = 0
		for letter in encrypted:
		  decrypted+=alphabet[keyList[t].index(letter)]
		  t = t + 1
		print(decrypted)
