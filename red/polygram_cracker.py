import sys
import random

text_list = []
mapped_list = []
ciphertext = ''

def read_ciphertext():
    ciphertext = [97, 98, 99, 100, 32, 101, 102, 103]
    print ciphertext
    return ciphertext

def convert_high_symbols(v):

    #print 'checking' + str(v)
    if v == 123: return 33  #!
    if v == 124: return 63  #?
    if v == 125: return 44  #,
    if v == 126: return 46  #.
    if v == 127: return 32  #Space

    return v

def generate_text_blocks():
    
    block_list = []

    for i in range(97, 128):
        for j in range(97, 128):
            for k in range(97, 128):
                for l in range(97, 128):
                    str1 = str(unichr(convert_high_symbols(i)))
                    str2 = str(unichr(convert_high_symbols(j)))
                    str3 = str(unichr(convert_high_symbols(k)))
                    str4 = str(unichr(convert_high_symbols(l)))
                
                    block_list.append(str1 + str2 + str3 + str4)

    return block_list

text_list = []
mapped_list = []

text_list = generate_text_blocks()
mapped_list = generate_text_blocks()
print text_list
print mapped_list
go_on = True

ciphertext = read_ciphertext()

while go_on:
    message = ''
    random.shuffle(mapped_list)
    
    for i in range(0, len(ciphertext), 3):
        cipher_snip = ''
        for j in range(0, 4):
            if i + j >= len(ciphertext):
                cipher_snip = cipher_snip + ' '
            else:
                cipher_snip = cipher_snip + str(unichr(ciphertext[i + j]))
        index = text_list.index(cipher_snip)

        message_snip = mapped_list[index]
        message = message + message_snip
    
    print message
