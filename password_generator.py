#Password generator
#importing random
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "(){},;:.-/\\?+*#$@&*'%"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

amount = int(input("How many password would you like:"))
length = int(input("What length would you like your password to be:"))

for x in range(amount):
    password = "".join(random.sample(all, length))
    print("Here is your passwords : " + password)