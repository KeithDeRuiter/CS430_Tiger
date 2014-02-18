with open('words.txt') as word_file:
	word_list = set(word.strip().lower() for word in word_file)

# checks if word is an english word
def is_word(word):
	return word.lower() in word_list