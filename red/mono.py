import string

with open("words.txt") as word_file:
	word_list = set(word.strip().lower() for word in word_file)

# checks if word is an english word
def is_word(word):
	return word.lower() in word_list

message = "IVK SV NT IKTT MZ WVS CTKTFP SV ORZS VII VWTZ OGRMWZ, NDS SV FMET MW R BRP SGRS KTZXTOSZ RWY TWGRWOTZ SGT IKTTYVC VI VSGTKZ.".lower()
cipher = "".join(l for l in message if l not in string.punctuation)

key = {}

print cipher