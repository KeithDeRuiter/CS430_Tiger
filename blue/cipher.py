import random
import copy
thing=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.','!','?']
random.seed(10)
listofthings=[]
for x in xrange(0,100):
  thing2=copy.deepcopy(thing)
  listofthings.append(thing2)
  random.shuffle(listofthings[x])
thing3="this is a message abcdefghijklmnopqrstuvwxyz !?."
thing4=""
for x in xrange(0,100):
  print(listofthings[x])
print(thing3)
t=0
for letter in thing3:
  thing4+=(listofthings[t][thing.index(letter)])
  t=t+1
print(thing4)
thing5=""
t=0
for letter in thing4:
  thing5+=thing[listofthings[t].index(letter)]
  t=t+1
print(thing5)