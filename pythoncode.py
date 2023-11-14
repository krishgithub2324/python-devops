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

#justt a text in local repo
 
