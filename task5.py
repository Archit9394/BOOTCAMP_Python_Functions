# 5.Write a program that accepts a sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

import sys

string1=sys.stdin.read() 
def make_upper(user_input):
    caps=user_input.upper()
    return caps

x=make_upper(string1)
print (x)