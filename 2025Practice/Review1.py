# 8/27/25

mystring = 'hello'
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# LISTS: 
#Exercise 1: 
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# exercise 2 : 
numbers = []
strings = []
names = ["John", "Oleg", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('adding')
strings.append('oz word')
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)