import itertools
import random
import sys

class Polygram():
	DIC = []
	SCRAMBLE = []
	CIPHERLEN = 1

	def __init__(self, blocklen):
		global CIPHERLEN, DIC, SCRAMBLE
		CIPHERLEN = blocklen
		DIC = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz.,!? ", repeat=CIPHERLEN)]
		SCRAMBLE = []
		SCRAMBLE.extend(DIC)
		random.seed(1337)
		random.shuffle(SCRAMBLE)

	def encrypt(self, CHUNK):
		LOC = DIC.index(CHUNK)
		return SCRAMBLE[LOC]

	def decrypt(self, CHUNK):
		LOC = SCRAMBLE.index(CHUNK)
		return DIC[LOC]

test = Polygram(3)
crypted = test.encrypt("abc")
decrypted = test.decrypt(crypted)
print(test.encrypt("abc"))
print(decrypted)
