#!/usr/bin/env python3
import sys
import secrets

def word_complex():
    rand = secrets.randbelow(369812)
    file = open("dict4schools/safedict_full.txt")
    lines = file.readlines()
    word = lines[rand]
    return word

def word_simple():
    rand = secrets.randbelow(40932)
    file = open("dict4schools/safedict_simple.txt")
    lines = file.readlines()
    word = lines[rand]
    return word

def complex():
    num = secrets.randbelow(3)
    randnums = secrets.randbelow(10)
    randnum = str(randnums)

    word1=word_complex()
    word2=word_complex()
    parsed_word1 = word1.rstrip()
    parsed_word2 = word2.rstrip()
    # print ("Word1: " + word1)
    # print ("Word1: " + word2)
    if num == 0:
        pass_text = parsed_word1 + parsed_word2 + randnum

    if num == 1:
        pass_text = parsed_word1 + randnum + parsed_word2

    if num == 2:
        pass_text = randnum + parsed_word1 + parsed_word2

    return(pass_text)

def simple(length=2,num_length=2):
    listpass = []
    num = secrets.randbelow(length)
    randnums = secrets.randbelow(num)
    randnum = str(randnums)

    count = 0
    while count < length:
        listpass.append(word_simple().rstrip())
        count += 1
    listpass.insert(num-1, randnum)
    gen_pass = undo_list(listpass)
    return(gen_pass)

# Turning a list back into text
def undo_list(input):
    undo_list = ''.join(input)
    return undo_list

# print(complex())
length=2
num_length=2
print (sys.argv[1])
if sys.argv:
    length = int(sys.argv[1])
    num_length = int(sys.argv[2])

else:
    exit
print(simple(length,num_length))
print(sys.argv)
