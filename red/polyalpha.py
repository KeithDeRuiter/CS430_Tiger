from collections import deque
import string

messages = 'Lknu hdlg av kqj drwkhrgfw';
messages = messages.lower().replace(" ", "");

dict = [line.rstrip() for line in open('words.txt')]

def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

# for chunk in chunks(messages, 4):
#     print chunk


for i in range(97, 128):
	for j in range(97, 128):
		for k in range(97, 128):
			for x in range(97, 128):
				for quadlet in chunks(messages, 4):
					a = ''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(quadlet, chr(i)+chr(j)+chr(k)+chr(x)))
					for word in dict:
						if a in word:
							print a
							print chr(i)+chr(j)+chr(k)+chr(x)





							
