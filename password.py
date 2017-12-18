#!/usr/bin/env python3
import os
import sys
import secrets
import argparse
import subprocess
from pathlib import Path
# import multiprocessing as mp

# Dimensions of screen
rows, columns = os.popen('stty size', 'r').read().split()

# Pass gen function
def gen_pass(length=2,num_length=2,complexity="simple"):
    listpass = []
    # Finding place to insert
    place_insert = secrets.randbelow(length)

    # Generating random number to insert
    randnums = secrets.randbelow(10**num_length)
    randnum = str(randnums)

    # Detecting complexity and finding length
    if complexity == complex:
        dict_lines = open_dict("safedict_full.txt")
    else:
        dict_lines = open_dict("safedict_simple.txt")

    # Finding length of dictionary
    dict_len = len(dict_lines)

    count = 0
    while count < length:
        listpass.append(gen_random(dict_lines,dict_len).rstrip())
        count += 1

    # Inserting number and undoing list
    listpass.insert(place_insert-1, randnum)
    gen_pass = undo_list(listpass)
    return(gen_pass)

def open_dict(dict_location):
    file_installed = Path("/etc/dict4schools/"+dict_location)
    file_cloned = Path("dict4schools/"+dict_location)
    if file_installed.exists():
        word_file = open("/etc/dict4schools/"+dict_location)
    elif file_cloned.exists():
        word_file = open("dict4schools/"+dict_location)
    else:
        print("Dictionary not found, exiting")
        exit(2)
    list_lines = word_file.readlines()
    return list_lines

def gen_random(dict_lines,dict_len):
    # Getting word
    line_number = secrets.randbelow(dict_len)
    word = dict_lines[line_number]
    return word

def check_blacklist(password):
    # Returns false if matches a word in blacklist
    black_list = open_dict("blacklists/blacklist_full.txt")
    black_list = [word.strip() for word in black_list]
    if any(word in password for word in black_list):
        return False
    else:
        return True

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

def open_dialog(passfile="password.txt"):
    subprocess.call(["open", passfile])

def output(password,count,passfile="password.txt"):
    if args.verbose:
        verbose = "true"

    # Display bar code
    disp_frac=" Progress: " + str(count)+'/'+str(amount)
    percentage=round((count/amount * 100),2)
    disp_percent=" " + str(percentage) + "%"

    # Code for the bar
    length=int(columns)-len(disp_frac)-len(disp_percent)
    length=length-4
    prog=round(percentage*length/100)
    togo=round((100-percentage)*length/100)

    # Split into two parts disp frac and remaining
    bar=" [" + "-"*prog + " "*togo + "] "

    # If output option was selected
    if args.output or args.save:
        pass_list = open(passfile,"a+")
        pass_list.write(password + "\n")

        # Only on last run
        if count == amount:
            print(disp_frac + bar + disp_percent)
            results_ciphertext = input("Do you want to open " + passfile + " [Y/N]")
            if results_ciphertext == "yes" or results_ciphertext == "y" or results_ciphertext == "Yes" or results_ciphertext == "Y":
                open_dialog(passfile)
    if not args.output or args.save:
        verbose = "true"

    if verbose == "true":
        print(" "*int(columns),end='\r')
        print(password)

    if not count == amount:
        print(disp_frac + bar + disp_percent, end='\r')

parser = argparse.ArgumentParser(description='A tool to generate random passwords.')
parser.add_argument('complex', help='Specifies if words should be taken from a complex dictionary.', action="store_true")
parser.add_argument("--num", "-n", type=int, help="Specifies the length of the randum number.")
parser.add_argument("--word", "--words", "-w", type=int, help="Specifies the number of words to be used.")
parser.add_argument("--amount", "-a", type=int, help="Specifies number of passwords to be generated.")
parser.add_argument("--output", "-o", type=str, help="Specifies file to output password to.")
parser.add_argument("--save", "-s", help="Save to password.txt", action="store_true")
parser.add_argument("--verbose", "-v", help="Shows the passwords made", action="store_true")
args = parser.parse_args()

# Default values
word_length = int(2)
num_length = int(2)
amount = int(1)
complexity = "simple"

# Setting argument variables
if args.word:
    word_length = args.word
if args.num:
    num_length = args.num
if args.amount:
    amount = args.amount
else:
    amount = 1
if args.save:
    passfile = "password.txt"

if args.output:
    passfile = args.output
else:
    passfile = "password.txt"

if args.complex:
    complexity = "complex"

# Loop multiple processes
# def loop(count):
#     password = gen_pass(word_length,num_length,complexity)
#     if check_blacklist(password):
#         output(password,count)
#     return count
#
# count = 0
# while count < amount:
#     processes = [mp.Process(target=loop(count))]
#     loop(count)
#     count += 1

# Multiple processes
# def worker(count):
#         password = gen_pass(word_length,num_length,complexity)
#         if check_blacklist(password):
#             output(password,count)
#
# for i in range(amount):
#     p = mp.Process(target=worker(i))
#     jobs = []
#     jobs.append(p)
#     p.start()

# original code
count = 0
while count < amount:
    count += 1
    password = gen_pass(word_length,num_length,complexity)
    if check_blacklist(password):
        output(password,count,passfile)

# Print done and close if pass_list is open
try:
    pass_list.close()
    print('Done!')

except:
    print('Done!')
