"""
#program-1 : Program to sum of n positive integer.
sum = 0
no = int(input("enter the no : "))
for i in range(1,no+1):
    sum = sum + i
print("sum of entered no:",sum)




#program-2 : program to count occurance of substring in string.

s = input("Enter any string : ")
print(s)
o = input("ener a substring which you want to count the occurance : ")

print("no of occurance of ",o, " : ",s.count(o))




#program-3 : program to count the occurance of each word in a given sentence


s = "Module 2 : Python Fundamentals"

d = dict()
s1 = s.split(" ")

for i in s1:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)



#program-4 :  program to get a single string from two given strings, separated by a space and swap the first 
#two characters of each string.

s1 = input("Enter any string 1: ")
s2 = input("Enter any string 2: ")

s = s1.split()+s2.split()
print(s)

new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

print(new_s1,new_s2)


#program-5 :  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string already ends with 'ing' then add 'ly' instead If the string length of the given 
#string is less than 3, leave it unchanged

s = input("enter string : ")
l = len(s)

if l>2:
    print("befor : ",s)
    if s[-3:]=="ing":
        s += "ly"
    else:
        s += "ing"
    print("after : ",s)

else:
    print(s)




#program -6 :  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
# Return the resulting string

s = input("enter a string : ")
sn = s.find("not")
sp = s.find("poor")

s = s.replace(s[sn:(sp+4)],"good")
print(s)



# Program to find Greatest Common Divisor of two numbers.


n1 = int(input("enter no 1: "))
n2 = int(input("enter no 2: "))

if n1>n2:
    smaller = n2
else:
    smaller = n1

for i in range(1,(smaller+1)):
    if n1%i == 0 and n2%i == 0:
        GCD = i
print("GCD of ",n1,"and ",n2,"is ",GCD)



"""

# Write a Python program to check if a number is positive, negative or zero
"""
n = int(input("enter any no"))
if n>0:
    print("no is positive")
elif n<0:
    print("no is negative")
else:
    print("it is zero1")


# Write a Python program to get the Factorial number of given number

n = int(input("enter no: "))
fact= 1
for i in range(1,n+1):
    fact = fact*i
print(fact)

# Write a Python program to get the Fibonacci series of given range.

n = int(input("enter no :"))
a=0
b=1 
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,n+1):
        c = a+b
        a=b
        b=c
        print(c)


# How memory is managed in Python?
# Python uses a portion of the memory for internal use and non-object memory.Another part of the memory is used for Python object such as int, dict, list, etc.


# What is the purpose continue statement in python?
# The continue statement is  skip the current iteration in a for loop or a while loop, and continues to the next iteration.


# Write python program that swap two number with temp variable and without temp variable.

a= int(input("enter no1: "))
b= int(input("enter no2: "))
t=a
a=b
b=t
#a,b=b,a
print("after swapping no1: ",a)
print("after swapping no2: ",b)


# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

n = int(input("Enter no : "))
if n%2==0:
        print("It is even")
else: 
        print("It is odd")


#Write a Python program to test whether a passed letter is a vowel or not.

a = input("enter alphabet:")
list=['a','e','i','o','u','A','E','I','O','U']
if a in list:
    print("it is vowel")
else:
    print("it is not vowel")


# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def sum(a,b,c):
    if a==b or b==c or a==c:
        sum = 0
    else:
        sum = a+b+c
        return sum
print(sum(1,3,4))



# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def value_check(a,b):
    if a==b or a-b == 0 or a+b==0:
        return True
    else:
        return False
print(value_check(5,0))


# Write a python program to sum of the first n positive integers.

sum = 0
no = int(input("enter the no : "))
for i in range(1,no+1):
    sum = sum + i
print("sum of entered no:",sum)


# Write a Python program to calculate the length of a string

s= input("Enter a string: ")
length= len(s)
print("length:", length)


#Write a Python program to count the number of characters (character frequency) in a string

string = input("Enter a string: ")
dict = {}
for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i]=1
print(dict)


# What are negative indexes and why are they used?
# The negative indexing is the act of indexing from the end of the list with indexing starting at -1 i.e. -1 gives the last element of list, -2 gives the second last element of list and so on.
# Negative Indexing is used in Python to begin slicing from the end of the string i.e. the last. Slicing gets a sub-string from a string. The slicing range is set as parameters i.e. start, stop and step.


# Write a Python program to count occurrences of a substring in a string.
s1 = input("Enter a string: ")
s2 = input("Enter a sub string: ")
count = s1.count(s2)
print(f"the substring '{s2}' occurs '{count}' in the string")


#Write a Python program to count the occurrences of each word in a given sentence

s = input("enter string: ")
d = {}
l = s.split(" ")

for i in l:
    if i in d:
        d[i] =+ 1
    else:
        d[i] = 1
print("word frequency: ",d)



# Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(w):
    max_len = 0
    for i in w:
        if len(w)>max_len:
            max_len = len(w)
    return max_len
w = ["lamborghini","Mercedes","BMW","Bugatti","Ferrari"]
longest_length = longest_word(w)
print("the length of longest word is : ",longest_length)


# Write a Python function to reverses a string if its length is a multiple of 4.

def mul_4_rev(string):
    if len(string) %4 == 0:
        return string[::-1]
    else:
        return string
string = input("enter the string: ")
print("length of string:",len(string))
result = mul_4_rev(string)
print(result)



# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def f_l_string(string):
    if len(string)>2:
        return string[:2] + string[-2:]
    
    else:
       return ''
string = input("enter string: ")
result = f_l_string(string)
print(result)
"""

# Write a Python function to insert a string in the middle of a string.

def ins_str(o_str,mid_str):
     mid_len = len(o_str)//2
     return o_str[:mid_len] + mid_str + o_str[mid_len:]
o_str = "python language"
mid_str = " programming "
print("orignal string: ",o_str)
print("insert string: ",mid_str)
new_string = ins_str(o_str,mid_str)
print("result string : ",new_string)