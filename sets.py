# A set is an unordered collection of items. Every element is unique (no duplication) and must be 
# immutable (which cannot be changed).

# A set is created by placing all the items (elements) inside curly braces{},
# sperated by commas.
# You can also use built in function set() to create sets.

# sets of integers
myset = {1,3,5}
print(myset)

# set of mixed datatypes
myset = {1,2.3,"hello",(1,2,4)}
print(myset)


# Creating Sets (part II)
# let's try to create a set with duplicate elements
myset = {1,2,1,2,12,3,4,3}
print(myset)

# as you can  see, myset doesn't have any duplicate elements.
# now let's create a set using the set() function.
