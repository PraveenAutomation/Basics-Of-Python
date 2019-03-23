#Indentation is mustand important
a=10
print(a+10)

if (a>10) :
	print("Pass")
else :
	print("Fail")

# No need to declare any data type of variable

i=52
print(i)

i=32.5
print(i)

i="Test"
print(i)

# Python is memory efficient --> pointing to same memory allocation in case:same value is refering 
x=50
y=x
print(x)
print(y)

# Now check the memory reference for both
print (id(x))
print (id(y))

# Variable declration Rule in Python
# It allows A-Z , a-z & 0-9
# It allows multiple assignment as well
miles =100.0
name='Praveen'
print(miles,name)

a=b=c=1
print(a,b,c)

a,b,c=2,7,'Mishra'
print(a,b,c)

# String Concept:Function,Concatnation etc.
s1='Hello Python'
print(s1)
print(s1[0])
print(s1[3:])
print(s1[2:5])
print(s1*2)
print(s1+" "+'World!!')



