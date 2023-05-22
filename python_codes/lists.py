"""In Python, a list is a collection of ordered and mutable elements. 
A list can contain elements of any data type, including other lists. 
Lists are created using square brackets [] or the built-in list() function."""

my_list = [1, 2, 3, 4, 5]

new_list = list(["a", "b", "c"])

primes = [2, 3, 5, 7, 11, 13]


"""Some key characteristics of lists in Python are:

Lists are mutable, meaning that you can add, remove, and modify elements in a list.
Lists are ordered, meaning that the order of elements in a list is guaranteed.
Lists can contain elements of any data type, including other lists."""


# Some common operations that can be performed on lists include:
# Accessing elements by index 
print(primes[0])  # returns the first element in the list

new_list[1] = "bee" # changes the value of the second element in the list
print(new_list)


primes.append(17) #adds the element 17 to the end of the list
print(primes)


my_list.remove(1) # removes the element 1 from the list
print(my_list)


primes[1:3] # slices a list; returns indeces [1], [2] BUT excludes [3]
# SLICING INCLUDES THE VALUE OF THE STARTING INDEX BUT EXCLUDES THE STOPPING INDEX

# You are free to insert multiple data types in one list, including another list

dynamic_list = [1, "string", 3.14159, True, ["another list", 1]]

# lists can contain duplicate values
dice_rolls = [3, 6, 6, 4, 5, 1, 4]


#You can also combine lists, known as concatenation

numbers = [1, 2, 3]
letters = ["a", "b", "c"]
numbers + letters

# Creating a list with a range of values
range_list = list(range(0, 10, 2))
print(range_list) # Output: [0, 2, 4, 6, 8]
"""The range() function generates a sequence of numbers from the starting value 
(0 in this case) up to, but not including, the ending value (10 in this case), 
with a step size of 2. The list() function converts this sequence into a list."""


#Sorting a list
list5 = [1, 2, 5, 4, 3, 6, 7, 8, 8, 3, 4, 5, 1, 2, 5, 2, 7, 8, 9, 9, 3, 4, 5]
list5.sort()
print(list5)

#Sorting a list in reverse
list5.sort(reverse=True)
print(list5)

#Concatenating lists
list11 = [1, 2, 3]
listA = ["a", "b", "c"]
print(listA + list11) # order matters when concatenating lists


#list comprehension
# You can create a new list from an already existing list
list14 = [1, 2, 3, 4, 5]
list15 = [x**3 for x in list14]
print(list15)