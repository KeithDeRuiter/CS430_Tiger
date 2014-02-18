import collections

with open("words.txt") as word_file:
	word_list = set(word.strip().lower() for word in word_file)

# checks if word is an english word
def is_word(word):
	return word.lower() in word_list

cipher = "T NEKZ ZD ZUE NDDOG PEWQMGE T NTGUEO ZD LTXE OELTPEHQZELB ZD IHDKZ DKLB ZUE EGGEKZTQL IQWZG DI LTIE QKO GEE TI T WDMLO KDZ LEQHK NUQZ TZ UQO ZD ZEQWU QKO KDZ NUEK T WQSE ZD OTE ZD OTGWDXEH ZUQZ T UQO KDZ LTXEO"
cipher = cipher.lower()
freq_string = "etaoinshrdlcumwfgypbvkjxqz"
key = {}

for letter in cipher:
	if not key.has_key(letter):
		key[letter] = '?'
key.pop(' ')

# count how many times each letter appears in the cipher, ignoring the spaces
frequency = collections.Counter(cipher)
frequency.pop(' ')

# use frequency data to fill out the key
while not len(frequency) == 0:
	next = frequency.most_common(1)[0][0]
	key[next] = freq_string[0]
	freq_string = freq_string[1:]
	frequency.pop(next)

for trans in key:
	cipher = cipher.replace(trans, key[trans].upper())

print cipher