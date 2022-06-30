# strings can be created by enclosing characters inside a single quote or double quotes. 
# Evan triple quotes can be used in Python  but it is generally use to represent multiple lines.

str = 'Hello world'
print(str)

str = "hello world"
print(str)

str = '''hello'''
print(str)

str ='''Hellow welcome
to the python world'''

print(str)


# similar to list and tuple, we can access characters in a string by using the index operatior []. here's howL:

str = "python"
print(str[0])

print(str[5])

# note indexing start from 0 

# python allows negative indexing for its sequences.

# the index of the lat character is -1, THE INDEX OF THE SECOND LAST CHARATER IS -2 and so on.

str = "program"
print(str[-1])

print(str[-len(str)])


# We can access a range of the characters in a string using the slicing operator.

str = 'Python'
print(str[1:4]) # gives you set of 2nd to 4rth characters


print(str[:4])
print(str[0:])

#Strings are immutable. it's not possible to change or delte characters of a string.
# However, you can delete the string entirely using the del keyword.

str = 'Python'
del str

print(str)


#Python String Operations
#There are many operations that can be performed with a string which makes it one of the most used data types in Python.

#Concatenation of Two Strings

#You can use the + operator to concatenate two strings.

first = 'Ri'
last = 'Bhar'

full = first+last
print(full)


# Repeat Two Strings
# You can repeat a string using * operator.

str = full
print(str*3)


# it's is important to note that we are not modifying strings. it's not possible. These operations create new strings.


# Iterating through a String

# Here's a program to count the number of 'l' in a string

count = 0

for letter in "Hello World":
    if letter == 'l':
        count+=1

print(count, "letters found")


# check whether Substring Exits

# we can test if a substring exits within a string or not, using the in keyword.

result = 'a' in "hello"
print(result)

result = 'ab' in "hello"
print(result)

result = 'abc' in "hello"
print(result)

result = 'ell' in "hello"
print(result)