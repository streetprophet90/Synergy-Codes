# In Python, a set is an unordered collection of unique and immutable objects. 

# create an empty set 
my_set = set()

# create a set with some values 
set2 = set([1, 2, 3, 4, 5, 6])

my_set2 = {1, 2, 3, 4, 5}

my_set3 =set(["1", 1, False])

"""Some Key characteristics of sets are: 
- sets are mutable, meaning you can add or remove elements from them
- sets are unordered, meaning the order of elements in the set are not guaranteed
- sets can only contain immutable objects, such as numbers, strings and tuples(containing only immutable elements)
- sets automatically remove duplicate values when created, so you can be sure that each element in a set is unique"""


# Some common operations that can be performed on sets include:

len(set2) #to know the number of items in a set

my_set.add(6) #to add an element to a set

my_set2.remove(1) # to remove an element from a set

my_set2.discard(3) # to discard an element from a set without an error warning if the element does not exist

my_set3.clear()



# COMBINING SETS
# Assuming we have a set of integers from 1 to 10

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([3, 5, 7])
composites = set([4, 6, 8, 9, 10])

#combining sets
print(odds.union(evens)) # this creates a union of oddss and evens

print(odds.intersection(composites)) #this creates an intersection of oddss and composites
                  

print(4 in odds) #checking if an element is in a set

print(odds.difference(evens)) #finding the difference between sets