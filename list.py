# append() to add an item to a list

# extend() to add all elements of a list to another list

# insert() to insert an item at a given index

# remove() to remove an itm from a list 

# pop() to remove an item at a given index

# clear() to remove all items from a list

# copy() to return a shallow copy of the list


# append extend
odd  = [1,3,5]

odd.append(3)
print(odd)

odd.extend([6,7,8,10])
print(odd)


my_list = ["p","y","t","h","o","n"]


# slicing 
print(my_list[1:3])
print(my_list[:3])
print(my_list[2:])
print(my_list[:])
 
# negative indexing

list = [1,2,3,4,5]

print(list[-1])
print(list[-2])
print(list[-3])
print(list[-5])


# + and * operator 
# concatination and multiplication

list1 = [1,2,3,4,5]

list1=list1+[6,7,8,9]
print(list1)

list2 = ["a","b","c"]

print(list2*3)

# insert(index_on_to_be_insert, element_to_inserted) 

list3 = [1,2,3]

list3.insert(1,10)
print(list3)

list3[2:2] = [5,7]
print(list3)


# updating indexes
list3[1:4] = [11,12,13]
print(list3)


# deleting element, range of element, entire list

list4 = [1,2,3,4,5,6]


del list4[1]
print(list4)

del list4[1:4]
print(list4)

del list4
# print(list4)


# remove() pop() clear()

list5 = [1,2,8,4,9,6,7,8,9,0]

list5.remove(8)  # remove first match found from list
print(list5)

list5.pop(3)  # remove element  at a given index
print(list5)

list5.pop()  # remove element at last index
print(list5)

list5.clear() # clear the list instead of deleting it
print(list5)


#  list copy 

list6 = [1,2,3]
list7 = list6

print(list7)

# copy()

list8 = [1,2,3]
list9 = list8.copy()

print(list9)
print(list9[0])

# check element in a list or not

list10 = [1,3,"the","is"]

print("the" in list10)
print("e" in list10)
print("is" in list10)