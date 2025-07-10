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


#6/18/25 Yo voy a atemptar a continuar mi practica de Python. En mismo tiempo, a veces, voy a aprender y practicar espanol. 
# Python shortcuts 

#1. F String 

palabra = "el tocador - closet"
print(palabra,"Tengo un tocador con los espejos largos.")
print(f"string {palabra}") # f stringifies variables 

#2. Unpacking 
'''A tuple in Python is an ordered, immutable collection of items. Tuples can hold elements of any data type, 
and once created, you cannot change (modify, add, or remove) the elements of a tuple.'''
la_comoda = (43,424,63,634)

a,b,c,d = la_comoda 
print (d,b,c,a)

el_sillon = {'sofa':1, 'armchair':2}
a,b = el_sillon.keys() #items (all) vs values (1,2) vs keys (sofa, armchair)
print (a,b)

#3 Mulit-assignmnet 

ancho, altura = "width", 'height' # can assign both values in one line 

ancho, altura = altura, ancho # re-assigning these values 
print (ancho, altura)

#4. Comprehensions 

anchoWidth = [altura for height in range(6)] # since i already decleared altura, it will use the assigned varialbe when printed 
print(anchoWidth)

alturaHeight = [i for i in range(10) if i % 2 == 0] # i serves as placeholder here i guess 
print(alturaHeight) # 

#5 Obejct multiplication 

x = "hello" * 5 
print (x)

y, b= [[1,2,3]] * 5, [4,6]*4 #nested list * 5 ..then normal list * 4 
y, b = b, y
print(y, b)
print (f'aqui es el string: {b}' )

# 6*********** INLINE / TERNARY CONDTION 
ancho = 1 if len(altura) > 3 else 3434
print(ancho, len(altura))
#_____vs: 
if 2 > 4 : 
    x = 1
else: 
    x = 434
    print(x)

#7 Zip - combines a list or collections together so you can iterate through them at the same time 

name = ['bbb', 'aaa']
ages = [43,53,23]
box = ['meidate', 'workout', 'kickboxing', 'read']
print(list(zip(name, ages, box))) #[('bbb', 43, 'meidate'), ('aaa', 53, 'workout')]

#8 *args and **kwargs
# this is a good shortcut to assign values to a list 
def function1(a,b,c):
    print(a,b,c)
words = [134,2,33]
function1(*words)

def fun2 (arg=None, arg2 = None, arg3 = None): # fucntion with parameters and print statment 
    print(arg, arg2, arg3)
kwargsexample = {'arg3':433, 'arg':535, 'arg2':932} # assigning values not in order 
fun2 (**kwargsexample)

#9 For Else & While Else statments 

buscar = [1,2,4,5]
objectivo = 34

for consejo in buscar:
    if consejo == objectivo:
        print('lo encontre') 
        break 
else: # else stmt will let you know if the element was found and you broke out of the for loop, or it was not found and you did not go through for loop 
    print("no existe")

#10 sort by key 
# if you want to sort the list by the second element in the list 

lst = [[1,2], [5,8], [7,3]]
lst.sort()
print(lst)# will just sort the list 
lst.sort(reverse = True) # reversed order 
print(lst)
# but they all sort based on the first number or character 
lst.sort(key=lambda x: x[1], reverse=True) # lambda is a one line funciton , x is a parameter returning x[1] index element 
print(lst)
# ******************************************************************************************************************************
#6/19/2025 DATA TYPES : 
# ******************************************************************************************************************************
#datatypes define the type of value that variable holds. 
#Integers and floats 
print (type(-12)) # type is used to print the data type of the value 

print(type (434 + 11.23))

#Boolean 
print(type (1 > 5))

#Strings 
multiline = """ # multi line 
La confianza es muy importante.
Pienso que para la obtener, 
neceista completar objectivos 
y entender 
y saber su characteristicas positivas. """

print(multiline)
#negating double quotes 
Alturaancho = """ quote's negation "is here" """
print(Alturaancho, altura, "printing %s" % (ancho))

callado = 'quiet'
print(callado[:5])
print(callado * 3)

# LISTS - are changable objects 
la_lista = [53,'Que Opina','How about that']
print(la_lista)
la_lista.append('merendar - to snack')
print(la_lista)

nested = ['recto','straight', ['permancer','to stay'], 'reir-to lough']
print(nested[2])#index two has a nested list element 

#tuple - also indexed; can't change or add anything to a tuple. 
### used when data will never change 

tuple_scoops = (1,2,3,4,6) 
print(tuple_scoops)

#sets 
extrano = {1,5,7}
print(list(zip(extrano, name)))

surge = {15,34,53,53}
emerge = {343,15,42,53}
print(surge | emerge)#get the distinct values between the two sets 
print(surge - emerge) # values in the lists that don't match 
print(surge ^ emerge) #completely unique values between the two sets 

#dictionaries 
#key/value pair 
acercarseToapproach = {'cruzar': 'cross','asegurar':'to assure', 'pegar':['to hit', 'odiar','to hate'] }
print(type(acercarseToapproach))
print(acercarseToapproach.values())
print(acercarseToapproach.items())#prints pairs 
print(acercarseToapproach['cruzar'])
acercarseToapproach['cruzar'] = acercarseToapproach['asegurar'] # updating dictionary value 
print(acercarseToapproach['cruzar'])
acercarseToapproach.update({'cruzar': 'cross','asegurar':'to assure', 'pegar':['to hit', 'odiar','to hate'] })
print(f"casting into a string {acercarseToapproach}")
print(type(acercarseToapproach))
print(type(f"casting into a string {acercarseToapproach}"))
del acercarseToapproach['asegurar'] # deleting a key and value from the dictionary 
print(acercarseToapproach)
