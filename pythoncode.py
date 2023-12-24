#input statement 

name=input("Enter your name:")
print(type(name))
print(name)


a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=a+b
print(type(c))
print(c)


a=float(input("Enter the a value:"))
b=float(input("Enter the b value:"))
c=a+b
print(type(c))
print(c)
 

 
name1,name2,name3=input("Enter the 3 names :").split(',')
print("name 1 : ",name1)
print("name 2 : ",name2)
print("name 3 : ",name3)


para=[25,35,34]
print(para[2])
print(type(para))


para=["25","35","34"]
print('|'.join(para))




para=[]
print("ENTER THE PARA :")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
    print(para)
    output='\n'.join(para)

print(output) 




#only for documentation
'''
only for documentation
only for documentationonly for documentation
only for documentation

'''


a=12.3
print(a)
print(type(a))

b=int(a)
print(b)
print(type(b))




a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
c=a+b
print("total : " + str(c))




#string and string function
s='sai Krish'
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('i'))
print(s.endswith('h'))
print(s.find('i'))
print(s.find('i',3))
print(s.replace('i','0'))




a= "saikrish"
print("is upper :", a.isupper())
print("is lower :", a.islower())
print("is alpha numeric :", a.isalnum())
print("is alpha :", a.isalpha())    

      



#split line function
a="he\nname\niskrish"
print(a)
print(a.splitlines())
print(a.splitlines(True))


#unwanted white space reomove panrathuku use panrathu

b="heyy,bubby,whatsup"
print(b.split(","))


c="heyy bubby whatsup"
print(c.split(" "))

 
d="      KRISH   "
print(len(d))
print(len(d.strip()))
print(len(d.lstrip()))
print(len(d.rstrip()))
print(len(d.strip().split()))


a='9-11-2023'
print(a.partition('-'))



#string manipulation
r='krishna'
print(r)
print(r[0:2])
print(r[:5])
print(r[1:])
print(r[-1])
print(r[-2:-1])
print(r[:-1])
print(r[::-1])

###  k  r  i  s  h  n  a
###  0  1  2  3  4  5  6
### -7 -6 -5 -4 -3 -2 -1

# this also called as an array slyzing

# arithmetic operators


### addition +
### subtraction -
### multiplication *
### division /
### modulus %
### ** exponentiation
### // floor division

a= 123
b= 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# assignment opperator

"""
= assignment opperator
 += addition 
 -= subtraction 
 *=multiplication 
 /= division 
 %=modulus 
 **=exponentiation
//= floor division
"""

a=2324
print(a)
a += 20
print (a)

a=2324
print(a)
a -= 20
print (a)

a=2324
print(a)
a *= 20
print (a)

a=2324
print(a)
a /= 20
print (a)

a=2324
print(a)
a %= 20
print (a)

a=2324
print(a)
a **= 20
print (a)

a=2324
print(a)
a //= 20
print (a)


# comprasion operator or relational operator

"""
== equal 
!= not equal
> greater than 
< less than 
>= greator than or equal to
<= less than or equal to
"""

a=23
b=24
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# logical operator in python
 
"""
and 
or
not 
"""
a=25
print(a>=10 and a<=20)
 
print(a>=10 or a<=20)

print(not(a>=10 and a<=20))


# bitwise operator
"""
 & and
 / or
 ^ xor 
 ~ not 
 << zero fill left shift
 >> signed right shift

"""
# lcm for a binary convertion
a=23
b=24
print( a & b )
print( a | b )
print( a ^ b )
print( ~a   )
print( a << 2 )
print( a >> 2 )


#if statement 

 #write a program to check the given number is no

k=int(input("enter the number:"))
if k % 2 == 0 :
    print (k, "number is even ")

# if else statement
        
else:
   print (k, "number is odd ")


   # if else statement
   
name = input ("enter your name : ")
age= int(input("enter your age :"))
if age >= 18 :   
    print (name, "age is ",age ,"elligable for vote ")
else:
    print (name, "age is ",age ,"not elligable for vote ")


# elif statement 
    
"""
0 no fine 
1-5  0.5
5-10  1
10-30  5
>30  membership cancel 
"""

days =int (input("enter the days:"))
if days == 0 :
    print ("good , no fine ")
elif days >= 1 and days <=5 :
    print("your fine amount: ",days * 0.5)
elif days >= 5 and days <=10 :
    print("your fine amount: ",days * 1)
elif days >= 10 and days <=30 :
    print("your fine amount: ",days * 5)
else:
    print("your membership is cancel")



# nested if statement
# 3 mark as input 
# total 
# average 
# result 
# if pass grade 
# 100 - 90 a
# 80- 89 b
# 70 - 79 c
# else d

m1=int(input("enter the m1 mark : "))
m2=int(input("enter the m2 mark : "))
m3=int(input("enter the m3 mark : "))
total = m1+m2+m3 
average = total / 3.0
print ("total : ",total)
print ("average : ",average)
if m1 >=35 and m2 >= 35 and m3 >= 35 :
 print ("result  pass")
 if average >= 90 and average  <=100 :
  print ("grade   A ")
elif average >=80  and average  <=89 :
   print ("grade  : B ")
elif average >= 70 and average  <= 79 :
   print ("grade  : C ")
else :
 print ("result : fail")
 print ("grade  d")



# while loop 
# 1 for loop
# 2 while loop


h=1
while h <= 10 :
    print (h)
    h+= 1
print ("----------------------")

t=3
while t<=20 :
    print (t)
    t += 3
print ("this is odd no ^^^^^^")

print ("----------------------")

t=2
while t<=20 :
    print (t)
    t += 2
print ("this is even no ^^^^^^")


# continue statement
y=1
while y <= 30:
    if y % 2 == 0 :
        y = y +1 
        continue;
print (y)
y += 1

 
 # break  statement
y=1
while y <= 30:
    if y  == 23 : 
        break
print (y)
y += 1

 
 # range in python

print(list(range (5)))
print(list(range (2,5))) #n-1
print(list(range (1,20,2)))
print(list(range (0,21,2)))

# for loop
for d in range (1,23,2):
    print (d)

for d in range (3):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    c=a+b-a
    print ("this is your value :",c)
        


# nested for loop

"""
*
**
***
****
*****
"""

for i in range(6):
    for j in range(i):
        print("$",end="") 
    print("")

print("--------------")

for i in range(5,0,-1):
    for j in range(i):
        print("$",end="")
    print("")

# A-Z > 65-90
# a-z > 97-122

for k in range(65,80,1):
    for d in range(65,80,1):
        print(chr(d),end="")
    print("")

    
# while else & for else
 
g=1
while g<=23000 :
    if g==20000:
       break
    print(g)
    g+=1
else:
    print("sucessful")

    

for m in range(1,21):
    if m == 7 :
        break
    print (m)
    
else:
    print(' loop completed')



# list in python 
# 1 sequence type
# 2 mutable

j=[1,2,3,4,5,6,7,8,9,10]
print(j)
print(type(j))
j[0]=2324
print(j)

print ('slicing')
print(j[1])
print(j[-1])
print(j[2:])
print(j[0:3])
print(j[:-5])
print(j[:4])
print(j[-1:])

s=[1,True,'krish',34.23,[1,2,3,3,44,5,5,6]]
print(s)
print(type(s))
print(s[0],"the type",type(s[0]))
print(s[1],"the type",type(s[1]))
print(s[2],"the type",type(s[2]))
print(s[3],"the type",type(s[3]))
print(s[4],"the type",type(s[4]))
print(s[4][2])

e = [23,34,53,45,64]
print(e)
e.clear()
print(e)

e = [23,34,53,45,64]
s = e.copy()
print (s)

e = [23,34,53,45,64,23]
print(e.count(23))
print(e.index(23)) # first element matton kandu pudikom
print(len(e))
print(min(e))
print(max(e))
print(e)
e.pop(0) # remove element using index
print(e)

e = [123,34,53,45,64,23]
e.remove(23) # remove values
print(e)

print('----------------------------')

names=["krish"]
print(names)
names.append("selva")
names.append("sai")
names.append("deepak")
print(names)

name2=[123,34,53,45,64,23]
names.extend(name2)
print(names)

names.insert(0,"suriya")
print(names)

print('---------------------------')

print(list(range(19)))
print(list("krishna"))

e = [123,34,53,45,64,23]
print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)
t=["Krish","Arun","Maisha","Sai","Selva","Deepak"]
t.sort() 
print(t)
t.sort(reverse=True)
print(t)

t=["Krish","Arun","Maisha","Sai","Selva","Deepak"]
t.sort(key=len) 
print(t)



# tuple in python
# imutable
# surrounded by round bracker ()

a=(1,2.3,True,"krish")
print(a)
print (type(a))
print(a[3])
print(a[-3])
print(a[0:2])
b=list(a)
print (b)
b.append("shevak")
print(type(b))
a=tuple(b)
print(a)
print(type(a))
 
for k in a:
    print(k)



if "krish" in a:
    print("krish is found")
else:
    print("krish  is not found")

print(len(a))

a=(2)
print(type(a))


a=(2,)
print(type(a))
del a
 
a=(1,2,3,4)
b=(5,6,7)
krish= a + b 
print (krish)
print(type(krish))

a=(1,2,7,3,4)
b=(5,6,7)
krish= a + b # or rlse use single letter
print(krish.count(7))

a=(1,2,7,3,4)
b=(5,6,7)
c=(a,b)
print(c)
print(c[0])
print(c[1])                     #nested tupple
print(c[0][2])

#tupple use pannratha iruntha use ,

k= ("krish",)*10000
print(k)
print(type(k))

a=(1,2,7,3,4)
print(max(a))
print(min(a))


# set function {}

names={"Krish","Arun","Maisha","Sai","Selva","Deepak"}
print(names)
print(type(names))          # we can remove can delet but we cant change 

for name in names :
    print(name)

# adding new element 
names.add("deekshika")
print (names)

# amother value
a={'dhilip','hari'}
names.update(a)
print(names)

names.remove('Sai')    # remove pannannuna use  S capital  
print(names)

names.discard('Sai')    # iruntha delete pannunu artham
print(names)

names.pop()
print(names)            # atho onu delete agom

names.clear()
print(names)

del names
print(names)


a={1,2,3,4,5}
b={'a','b','c'}
c=a.union(b)
print(c)
a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)





