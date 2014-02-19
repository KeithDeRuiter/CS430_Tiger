import itertools
import random
import sys

class Polygram:
	DIC = []
	SCRAMBLE = []
	CIPHERLEN = 4

	def __init__(self):
		self.DIC = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz.,!? ", repeat=self.CIPHERLEN)]
		self.SCRAMBLE = []
		self.SCRAMBLE.extend(self.DIC)
		random.seed(1337)
		random.shuffle(self.SCRAMBLE)

	#Function that splits input string into blocks of size SIZE
	def splitter(self, CHUNK, SIZE):
		return [str(CHUNK[i:i+SIZE]) for i in range(0, len(CHUNK), SIZE)]

	def encrypt(self, CHUNK):

		clean = str(CHUNK).rstrip()
		#Split message into x length blocks
		message = self.splitter(clean, self.CIPHERLEN)

		#Make sure last block is 3 length or append spaces to make it so
		while(len(message[-1]) < self.CIPHERLEN):
			message[-1] = message[-1] + " "

		#Encrypt each block
		messageCrypt = ""
		for i in range(len(message)):
			LOC = self.DIC.index(message[i])
			messageCrypt += self.SCRAMBLE[LOC]

		#Return full message
		print(messageCrypt)
		return messageCrypt 

	def decrypt(self, CHUNK):
		#Split message into x length blocks
		message = self.splitter(CHUNK, self.CIPHERLEN)

		#Decrypt each block
		messageDecrypt = ""
		for i in range(len(message)):
			LOC = self.SCRAMBLE.index(message[i])
			messageDecrypt += self.DIC[LOC]

		#Remove any extra spaces at end that were added for padding
		messageDecrypt = messageDecrypt.strip()
		#Return full message
		print(messageDecrypt)
		return messageDecrypt
