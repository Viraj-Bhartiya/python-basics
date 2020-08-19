
# Variables
x = 2  #int datatypr
y = 3
name = "Viraj Bhartiya" # String datatype
age = 15.32 # float/ double datatype


# Various print Functions
print("50 * 100 = ",50*100)
print("{0} + {1} = {2}".format(x,y,x+y))
print("Viraj","Bhartiya", sep=" ") # Seperates it by a ' ' 
print("Hello, %s" %name) # %s for Strings ... %d for digiys
print("Hello, %s ! you are %d old" %(name,age)) #name refers to line 5 and age refers to line 6

x = "hello"
y = "hello"
print(x[0:3]) # prints hel... indexing in programming is from 0
print(y.upper) # prints it in uppper care
print(y.lower) # prints everything in lowercase
''' 
Suggestion: just type the varible name in print and add a period '.'... example(print.)
it will show u a list of funtions which can b used 
'''

'''
this is a multiline comment
'''
# this is a single line comment

#comment lins are not read during running the program


print(dir(__builtins__)) #to print built ins
print (help) # to print help of a specefic function

#importing a lib.
import math
print(math.sqrt(25))
print(dir(math))

#Simple prog. to print largest no.
x = int(input("enter a no ")) # this takes the input and stores it in variable x
y = int(input("enter a no "))#this in y
z = int(input("enter a no "))# this in z

n = max(x,y,z) #returns the max value among x,y,z
print(n) 
  

 # conditional statements
  
# if - else-if
x = 100
if x == 10 : # if c == 10 print true
    print("true")
elif x == 100 : # else if x == 10 print hi
    print("hi")
else: # if none of the aboe are ture print false
     print("false")



# list aka array
# used to store multiple values of same datatype
x  = [1,2,3,4]

#to print length of list
print(len(x))

#to remove a element fron a list....removes the element not the element at that index
x.remove(2)
print(x)

#to insert a element in a list
x.insert(1,2)
print(x)

#pop removes the last element
print(x.pop())
print(x)

# delets the var
del x
#print(x)

#clears the elements of the list
x = [1,2,3,4]
x.clear()
print(x)

#sorts the list in ascending arder
x = [3,5,2,1,9]
print(x)
x.sort()
print(x)

#reverses the order of the list
x.reverse()
print(x)

#adds the valve at last
x.append(10)
print(x)

#copy the list to other var
z = x.copy()
print(z)

#prints the no of similar elements
z.append(10)
print(z.count(10))

#adds two lists
print(x+z)

#to print max value in a list
print(max(x))



#touple
#similar to list but these cannot b deleted/edited
x = (1,2,3,4)
print(x)

#to print a value stored at a specefic index
print(x[2])

print(x.count(1))
print(len(x))

#to add two touple
y = (9,8,7)
z = x + y
print(z)


#to save a specific value multiple times
a = ('hi','by',)*5
print(a)

#to print max value in  a touple
print(max(z))

#to delete a touple
del z





#set
#removes the duplicate values

x = {1,2,3,5,9,2,4,2,3,4}
print(x)

x.add(10)
print(x)

x.update({15,2,5,11,4,45,2,})
print(x)

x.remove(15)
print(x)

x.discard(11)
print(x)

#removes any random element
x.pop()
print(x)

x.clear()
print(x)

#del x

z = set((2,12,323,21,21,21,11,2,121,2,1))
print(z)

# converts list to set
z = {[1,2,3,4]}
print(z)

#union of 2 sets
print(x | z)
x.union(z)
print(x)

#prints similar elements of a set
x.intersection(z)
print(x & z)

#prints values which are different
print(x-z)
x.difference(z)
print(z-x)

#prints symetric difference
print(x ^ z)
print(x.symmetric_difference(z))

#sets are not indexed




#dictionary
# they take a key and a value pair
a = {'name':'Viraj','year':5,'age':15}
print(a)
print(a['name']) #prints the vlue pair of the key 'name'

print(a.get('year'))
print(len(a))

a['Surname'] = 'Bhartiya'
print(a.get('Surname'))

a.pop('Surname')
print(a)

a['name'] = 'Citrus'
print(a['name'])

a.update({'name':'Viraj'})
print(a['name'])

print(a.keys()) # prints all th keys

#removes last item
a.popitem()
print(a)

a.clear()
print(a)

del a
#you can store any kind of values in dictionary


#slice
a = [1,2,3,4,5,6,7,8,9]
b = (1,2,3,4,5,6,7,8,9)
c = '123456879'

x = slice(0,5)

print(a[x])
print(a[0:5])

'''
a[start:end]  start to end-1
a[start:]     start to end of list
a[:end]       from begining to end -1
a[:]          whole array
a[start:end:step]start through not past end,by step

print these for better understanding
'''

#negative index
"""
P  Y  T  H  O  N
0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
"""



#while loop
i = 0
while i <= 5 :
    print("The value of i is : ",i)
    i += 1
print("loop Finished")


num = 0
sum = 0

print("Enter 0 to exit the loop")

while i != 0:
    num = float(input("Enter a no : "))
    sum += num

    if num == 0:
        break
else :
    print(" Loop Finished")
print("Sum :",sum)



#for loop
a = [0,1,2,3,4,5] # list
b = (0,1,2,3,4,5) #tuple
c = {0,1,2,3,4,6} #set
d = '012345'      #string
e = { #dictionary
    'name':'Viraj',
    'Age':15
}

#in operator
#in gives values t/f 

print(0 in a)
print(1 in b)
print(2 in c)
print('3' in d)

for x in a :  #can be tried with b,c,d
    print(x)

# 'for' loop for dictionary

for x in e.keys(): #can b used with .values() , .items()
    print(x)

for key,value in e.items() :
    print(key,' ',value)

for x in range(10):  #for(int x = 0;x<10;x++)
    print(x)

for x in range(1,10): #for(int x = 1;x<10;x++)
    print(x)

for x in range(1,10,2): #for(int x = 1;x < 10; x+=2)
    print(x)
else :
    print(" Loop Finished")
#the comments are java references

#break continue
a = [0,1,2,3,4,5]

for x in a :
    if x == 3 :
        break #terminates the execution of loop
    print(x)


i = 0
while i < 5 :
    if i == 3:
        continue # skips the execution
    print(i)
    i += 1