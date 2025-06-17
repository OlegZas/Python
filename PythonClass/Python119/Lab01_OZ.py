# This is Oleg's Python practice file. Let the games begin! 
#6/16/25
name = "Olegario"
lastname = "Erudito"

print('Hello')
print("Hello Little Dudes")
print("Hello, and welcome to the realm of: %s" % (name)) # %s placeholder for a string , %i for integer 
#alternative placeholder 
keyword = "Resillient"
print("I consider myself to be a {} person.".format(keyword))


x = 456
y = 2

if x%y != 0: #REMEMBER: == equals, = assignment 
    print("Learning already")
else:
    while y < 5:
        print("%s testing and trying nested loop in condtional statment" % (name))
        y +=1 # REMEMBER:  instead y = y+1 just do y += 1
