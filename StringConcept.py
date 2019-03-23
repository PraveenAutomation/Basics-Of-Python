# String Declration in Python
s1="Test Selenium"
s2='Hello Python'
print(s1,s2)

#Print length of String
print (len(s1))
print(s1[2:])
print(s1[0:5])
# print(s1[23]) Error: IndexError: string index out of range

#For Space & Tab
print('Praveen \n Mishra') #Space
print("Praveen \t Mishra") # Tab

# Print String multiple time
print('vanu'*3)

# 'in' and 'not in' Operator
print('Test' in s1)
print("java" in s2)
print("Python" not in s2)

# Formatting operator
print("my name is %s and my age is %d " %('Tom',25)) 
		#O/P: my name is Tom and my age is 25 

# Writing paragraph in python either use triple quote single (''' ''') or(""" """") 
s3='''python is excellent 
language and very easy'''
print(s3)

s4="""I am learning python 
and i am very happy"""
print(s4)

# Escape Apostrophee problem(String literals)
s5='Hi I\'m praveen'
print(s5)
print("Hi my fav lang is \"Python\" and so happy")