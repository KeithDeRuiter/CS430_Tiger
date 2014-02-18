with open("words.txt") as word_file:
	word_list = set(word.strip().lower() for word in word_file)

pattern_dict = {}

for word in word_list:
	count = 'A'
	pattern = word

	for letter in pattern:
		if letter.islower():
			pattern = pattern.replace(letter, count);
			count = chr(ord(count)+1)

	if not pattern_dict.has_key(pattern):
		pattern_dict[pattern] = {word}
	else:
		pattern_dict[pattern] |= {word}

pattern_dict["A"] = {'a', 'i'}
pattern_dict["AB"] = {'of', 'to', 'in', 'it', 'is', 'be', 'as', 'at', 'so', 'we', 'he', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am'}

print pattern_dict["AB"]