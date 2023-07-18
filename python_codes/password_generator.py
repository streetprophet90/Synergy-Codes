#!/usr/bin/python3

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# get nr_letters random numbers b/n 0 and 51 of letters from letters list

selected = []

# run this loop nr_letters times to get nr_letters random letters
# store them in the list letters_sel

for lett in range (0, nr_letters):
  x = random.randint(0, (len(letters)-1))
  selected.append(letters[x])

# do same for symbols
for symb in range(0, nr_symbols):
  x = random.randint(0, (len(symbols)-1))
  selected.append(symbols[x])

# repeat for numbers
for num in range (0, nr_numbers):
  x = random.randint(0, (len(numbers)-1))
  selected.append(numbers[x])
print(*selected, sep="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
shuffled = random.shuffle(selected)
print(*selected, sep="")



