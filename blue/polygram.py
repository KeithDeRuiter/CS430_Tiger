import itertools
import random
import sys

class Polygram:
	DIC = []
	SCRAMBLE = []
	CIPHERLEN = 4

	def __init__(self):
		global CIPHERLEN, DIC, SCRAMBLE
		DIC = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz.,!? ", repeat=CIPHERLEN)]
		SCRAMBLE = []
		SCRAMBLE.extend(DIC)
		random.seed(1337)
		random.shuffle(SCRAMBLE)

	#Function that splits input string into blocks of size SIZE
	def splitter(self, CHUNK, SIZE):
		return [CHUNK[i:i+SIZE] for i in range(0, len(str), SIZE)]

	def encrypt(self, CHUNK):
		#Split message into x length blocks
		message = splitter(CHUNK, CIPHERLEN)

		#Make sure last block is 3 length or append spaces to make it so
		if(len(message[-1]) == 1):
			message[-1] = message[-1] + "  "
		elif( len(message[-1]) == 2):
			message[-1] = message[-1] + " "

		#Encrypt each block
		messageCrypt = ""
		for i in range(len(message)):
			LOC = DIC.index(message[i])
			messageCrypt += SCRAMBLE[LOC]

		#Return full message
		return messageCrypt 

	def decrypt(self, CHUNK):
		#Split message into x length blocks
		message = splitter(CHUNK, CIPHERLEN)

		#Decrypt each block
		messageDecrypt = ""
		for i in range(len(message)):
			LOC = SCRAMBLE.index(CHUNK)
			messageDecrypt += DIC[LOC]

		#Return full message
		return messageDecrypt
