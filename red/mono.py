import string
import copy
import collections
import sys
from itertools import chain, combinations

# maps a->0, b->1, ect
def to_num(char):
	return ord(char)-97

def to_char(num):
	return chr(num+97)

def powersets(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range (len(s)+1))

def subsets(s):
	return map(set, powersets(s))

pattern_dict = {}

# read the pattern dictionary
with open('pattern_dict.txt') as pattern_file:
	lines = pattern_file.readlines()
	is_pattern = True;
	cur_pattern = '';
	for line in lines:
		line = line.rstrip()
		if is_pattern:
			is_pattern = False
			cur_pattern = line
			pattern_dict[cur_pattern] = set()
		else:
			if line == "#":
				is_pattern = True
			else:
				pattern_dict[cur_pattern] |= {line}

message = 'THERE IS NOTHING THAT I WANT MORE THAN TO GO TO $NIVERSITY AND BECOME A PROFESSOR I WILL GO TO THE BOOKSTORE AND P$RCHASE A TON OF BOOKS.'.lower()

#with open(sys.argv[1]) as msg_file:
#	message  = msg_file.read()

count = 'A'

new_message = message

for c in message:

	if c in ',.?!abcdefghijklmnopqrstuvwxyz':
		continue


	for d in ',.?!abcdefghijklmnopqrstuvwxyz':
		if not d in new_message:
			new_message = new_message.replace(c, d)
			break

message = new_message

# find the space character
# the character with the least likely value is probably the space
most_likely = 99999
for c in ',.?!abcdefghijklmnopqrstuvwxyz':
	test_words = message.split(c)
	likely = 0
	for tw in test_words:
		# if two of the same character is next to each other, it can't be the space
		if len(tw) == 0:
			likely += 10000
		# each instance of a word longer than 11 makes it less likely to be the space
		if len(tw) > 11:
			likely += len(tw) - 11
		# each instance of a word longer than 16 makes it much less likely to be the space
		if len(tw) > 16:
			likely += (len(tw) - 16) * 4
	if likely <= most_likely:
		space_char = c
		most_likely = likely

# find the punctuations
punct = set()
punct.add(message[-1])
for c in ',.?! abcdefghijklmnopqrstuvwxyz':
	is_punct = True
	#if c not in message.replace(message[-1], ''):
	if c not in message:
		is_punct = False
		continue
	test_words = message.split(space_char)
	for tw in test_words:
		if c in tw[:-1] or c == tw:
		#if c == tw:
			is_punct = False
			continue
	if is_punct:
		punct.add(c)

if space_char in punct:
	punct.remove(space_char)

new_ciphers = []

for ss in subsets(punct):
	print ss

for p_set in subsets(punct):
	if len(p_set) > 4:
		continue
	#if not message[-1] in p_set:
	# 	continue
	new_cipher = message.replace(space_char, '-')
	for p in p_set:
		new_cipher = new_cipher.replace(p, '')
	new_ciphers.append(new_cipher)

final_ciphers = []

for c in new_ciphers:
	count = 'A'

	# determine the pattern
	for letter in range(len(c)):
		if (c[letter].islower() or c[letter] in ',.!?') and c[letter] != '-':
			c = c.replace(c[letter], count);
			count = chr(ord(count)+1)
	c = c.replace('-', ' ')
	final_ciphers.append(c)

for trial_cipher in final_ciphers:

	trial_cipher = trial_cipher.lower()
	cipher = ''.join(l for l in trial_cipher if l not in string.punctuation)
	words = cipher.split(' ')

	# set up the key to have every possibility
	key = []

	for letter in 'abcdefghijklmnopqrstuvwxyz':
		alphabet = set()

		if letter in cipher:
			for l in 'abcdefghijklmnopqrstuvwxyz':
				alphabet.add(l)
			key.append(alphabet)
		else:
			alphabet.add('-')
			key.append(alphabet)

	# the initial dictionary attack run through
	# for every word in the cipher
	for word in words:
		count = 'A'
		pattern = word

		# determine the pattern
		for letter in pattern:
			if letter.islower():
				pattern = pattern.replace(letter, count);
				count = chr(ord(count)+1)

		# for every letter in the word, determine the possible mappings based on dictionary patterns
		letter_id = 0
		for letter in word:
			possible_set = set()
			# for every possibility (possible word determined by the given pattern)
			try:
				for possibility in pattern_dict[pattern]:
					possible_set.add(possibility[letter_id])
			except KeyError:
				continue
			letter_id += 1
			key[to_num(letter)] = key[to_num(letter)] & possible_set


	# refine 10 times, if its not finished after 10 times you might as well give up
	for i in range(10):

		# remove letters you have already sloved from the rest of the possibilities
		for i in range(26):
			if len(key[i]) == 1:
				for j in range(26):
					if len(key[j]) > 1:
						key[j] = key[j] - key[i]

		for word in words:
			count = 'A'
			pattern = word

			for letter in pattern:
				if letter.islower():
					pattern = pattern.replace(letter, count);
					count = chr(ord(count)+1)

			try:
				possible_words = copy.deepcopy(pattern_dict[pattern])
			except KeyError:
				continue

			# get the letters we have already solved
			solved_letters = []
			solved_word = ''
			for i in range(len(word)):
				if len(key[to_num(word[i])]) == 1:
					solved_letters.append(key[to_num(word[i])])
				else:
					solved_letters.append(set(['-']))

			for i in solved_letters:
				for e in i:
					solved_word += e

			# find the words that don't matched the new patterng
			to_remove = set()
			for wrd in possible_words:
				for i in range(len(wrd)):
					if solved_word[i] != '-' and solved_word[i] != wrd[i]:
						to_remove.add(wrd)
						break

			# filter possibilities based on new information
			letter_id = 0
			for letter in word:
				possible_set = set()
				for possibility in possible_words - to_remove:
					possible_set.add(possibility[letter_id])
				letter_id += 1
				key[to_num(letter)] = key[to_num(letter)] & possible_set


	# solve the cipher message
	i = 0
	for answer in key:
		if len(answer) > 0:
			trial_cipher = trial_cipher.replace(to_char(i), answer.pop().upper())
		else:
			trial_cipher = trial_cipher.replace(to_char(i), '?')
		i += 1

	print trial_cipher
