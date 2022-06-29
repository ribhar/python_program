

# a tuple is similar to a list. the difference between the two is that we cannot change the elements of a tuple once
# it is assigned whereas, in list elements can be changed.

# tuples can be created placing all the items (elements) inside parentheses (), separated by commas.

# A tuples can have any number of items and the may be  different types (integer,float,list,sting etc.).


my_tuple = () # empty tuple

my_tuple = (1,2,3) # tuple having intergers

my_tuple =  (1, "Hello", 3.4) # mixed data tuple

my_tuple = ("cat",[2,4],(1,3,5)) # nested tuple

# A tuple can also be created without using parantheses. However, it's a good practice to use them.

my_tuple = 3, 4.6,"dog"

print(my_tuple)


# Creating Tuples With One Item

# Creating a tuple with one is a bit tricky

# Having one item within parantheses is not enough. We will need a tailing comma to indicate that it is in fact a tuple.


# only parantheses is not enough
t1 = ("hello")
print(type(t1))

# need a comma at the end
t2 = ("hello",)
print(type(t2))

# parantheses is optional
t3 = "hello",
print(type(t3))

odd = (1,2,3,4,5)

print(odd + (1,2,4,5))
print(odd*3)

# tuples are immutable

odd1 = (1,2,3,4,4)
# odd1[2] = 3 / it will give you error

# however elements for tuple are mutalble

odd3 = (1,2,["a","2","a"])
odd3[2][0] = "2"
print(odd3)


# deletion of element is not posible in tuple
# del odd3[1] / this will give and error

# however we can delete tuple it self
del odd3
print(odd3)
