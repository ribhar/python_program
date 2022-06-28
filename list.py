
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