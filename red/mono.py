import string
import copy

# maps a->0, b->1, ect
def to_num(char):
	return ord(char)-97

def to_char(num):
	return chr(num+97)

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

message = 'LY LZ RIYYIV YF PIQJ KVFD RINLHJ QHJ YF OSY FYNIVZ LH KVFHY, IZOIALQPPU XNIH UFS AIPIRVQYI CLAYFVU XNIH HLAI YNLHTZ FAASV. UFS YQGI YNI KVFHY PLHI XNIH YNIVI LZ JQHTIV. YNIH OIFOPI XLPP QOOVIALQYI UFSV PIQJIVZNLO'.lower()
cipher = ''.join(l for l in message if l not in string.punctuation)
words = cipher.split(' ')

print message

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
		possible_set = set()c
		# for every possibility (possible word determined by the given pattern)
		for possibility in pattern_dict[pattern]:
			possible_set.add(possibility[letter_id])
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

		possible_words = copy.deepcopy(pattern_dict[pattern])

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

		# find the words that don't matched the new pattern
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
	message = message.replace(to_char(i), answer.pop().upper())
	i += 1

print message