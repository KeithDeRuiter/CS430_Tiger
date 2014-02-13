import itertools
import random

DIC = []
SCRAMBLE = []
CIPHERLEN = 3

def encrypt(CHUNK):
	global DIC, SCRAMBLE
	LOC = DIC.index(CHUNK)
	return SCRAMBLE[LOC]

def decrypt(CHUNK):
	global DIC, SCRAMBLE
	LOC = SCRAMBLE.index(CHUNK)
	return DIC[LOC]

def setup():
	global DIC
	DIC = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz.,!? ", repeat=CIPHERLEN)]
	SCRAMBLE.extend(DIC)
	random.seed(1337)
	random.shuffle(SCRAMBLE)

setup()
print(DIC)
test = encrypt("abc")
print(test)
back = decrypt(test)
print(back)
