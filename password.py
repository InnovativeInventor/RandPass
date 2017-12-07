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

def complex(length=2,num_length=2):
    listpass = []
    num = secrets.randbelow(length)
    randnums = secrets.randbelow(10**num_length)
    randnum = str(randnums)

    count = 0
    while count < length:
        listpass.append(word_complex().rstrip())
        count += 1
    listpass.insert(num-1, randnum)
    gen_pass = undo_list(listpass)
    return(gen_pass)

def simple(length=2,num_length=2):
    listpass = []
    num = secrets.randbelow(length)
    randnums = secrets.randbelow(10**num_length)
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

def help():
    print()
    print("Usage:")
    print(sys.argv[0] + " <number of words> <digits of random number>")
    print()
    print("Contributions are welcome!")
    sys.exit(1)

def cli_args(length=2,num_length=2):
    # Command-line Args
    if len(sys.argv) == 3:
        length = int(sys.argv[1])
        num_length = int(sys.argv[2])

    # Detect simple vs complex vs full
    elif str(sys.argv[1]) == 'complex' or str(sys.argv[1]) == 'c' or str(sys.argv[1]) == '--complex' or str(sys.argv[1]) == '-c':
        gen=complex(length,num_length)
        print ("complex")

    # Detect help
    elif str(sys.argv[1]) == 'h' or str(sys.argv[1]) == 'help' or str(sys.argv[1]) == '-h' or str(sys.argv[1]) == '--help':
        help()

    elif len(sys.argv) == 2:
        print("Error: Incorrect number of arguments provided.")
        print("If you are going to pass options, please see the output of -help below.")
        help()
    return gen

length=int(2)
num_length=int(2)

try:
    len(sys.argv)
    args="true"

except:
    args="false"

if args == "true":
    gen = cli_args()
else:
    gen=simple(length,num_length)

print(gen)

# ## todo
# Errors: ./password.py complex 3
