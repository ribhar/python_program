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
