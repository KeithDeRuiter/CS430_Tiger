import random
import copy
#list of the alphabet we are using
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
random.seed(10)
#list of 100 monoalphabetic keys
keyList=[]
#this copies the alphabet and then shuffles it 100 times for 100 keys
for x in xrange(0,100):
  thing=copy.deepcopy(alphabet)
  keyList.append(thing)
  random.shuffle(keyList[x])
message="this is a message abcdefghijklmnopqrstuvwxyz !?."
encrypted=""
print(message)
t=0
#encrypts message polyalphabetically (doing it monoalphabetically just means you dont increment t)
for letter in message:
  encrypted+=(keyList[t][alphabet.index(letter)])
  t=t+1
print(encrypted)
decrypted=""
t=0
for letter in encrypted:
  decrypted+=alphabet[keyList[t].index(letter)]
  t=t+1
print(decrypted)
