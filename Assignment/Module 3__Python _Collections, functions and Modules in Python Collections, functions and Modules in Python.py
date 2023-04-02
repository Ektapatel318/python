"""
# program-8 : Write a Python program to check whether a list contains a sublist

list = ["Python",11,"tops","technology", 12,10,14,13]
s_list = ["Python","tops", 10,14]
result = []

print(list)
print(s_list)


for i in range(len(s_list)+1): 
    if s_list[i] in list:
        result = s_list[i]     

    else:
        
        print("not a sublist") 

print("yes it contain sublist",reslut)    


# program-9 : Write a Python program to find the second smallest number in a list.

lst = [21,34,67,11,45,0,87,93]
lst.sort()
print("second smallest number is  :",lst[1])

#lst = [21,34,67,11,45,0,87,93]
#print("second smalllest number is ", sorted(lst)[1])


# program-10 : Write a Python program to get unique values from a list.

def uniquel(lst):
    return list(set(lst))

my_list = [2,43,1,2,4,6,4,32,45,44,45,4,5,2]
print(uniquel(my_list))



# program-11 : Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))


#program-12 : Write a Python program to convert a list of tuples into a dictionary

lst = [("x",1),("y",2),("x",5)]
d= {}
for a,b in lst:
    d.setdefault(a, []).append(b)
print(d)


#program-13: Write a Python program to sort a dictionary (ascending /descending) by value.
import operator
d ={2:4,4:6,1:5,5:1,0:0}
print("original dictionary",d)
a_dic = sorted(d.items(), 
             key = operator.itemgetter(1))

s_dic   = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print(a_dic)
print(s_dic)


#program- 14: Write a Python program to find the highest 3 values in a dictionary

from collections import Counter

dic ={ 'e1': 11, 'e2':56, 'e3':45 , 'e4': 44, 'e5':80, 'e6':78, 'e7':90    }
k = Counter(dic)
max_dic = k.most_common(3)
print("initial dictionary:")
print(dic,"\n")

print("dictionary with highest 3 values: ")
print("keys : values")

for i in max_dic:
    print(i[0]," :",i[1]," ")

#----------------------------------------------------------------------------------------------------------------------
#program-15 :Given a number n, write a python program to make and print the list of Fibonacci series up to n.


def fibo(num):
    if num == 1:
        return 1 
    else:
        a=0 
        b=1
        print(a)
        print(b)
        for i in range(num):
            c = a+b
            print(c)
            a=b
            b=c
        
n= int(input("enter the no : "))
(fibo(n))

#--------------------------------------------------------------------------------------------------------------------

# What is List? How will you reverse a list?
# list is a collection of data type. which is used to store multiple data elements in to a single variable.
# it is sperated by commas and enclose by a square brackets. it is mutable,ordered and indexable.



# How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
#l = [1,3,4,5,6,7,8,9,10]
#l.pop(-1)
#print(l)



## Differentiate between append () and extend () methods? 
# append() method adds a single element to the end of the list, while extend() method adds multiple elements to the end of the list.
# append() method modifies the original list by adding the new element as a single item, while extend() method modifies the original list by adding each element of the iterable as individual items to the end of the list.
#l1= [1, 2, 3]
# l2 = [4, 5, 6]
# l1.append(l2)
# print(l1)  
# l1.extend(l2)
# print(l1)  
    



# Write a Python function to get the largest number, smallest num and sum of all from a list.
def operation_fuc(lst):
    max_num = max(lst)
    min_num = min(lst)
    total = sum(lst)
    return max_num,min_num,total

lst  = [11,45,33,78,45,67,78,98]
max_n,min_n,sum = operation_fuc(lst)
print("maximum no : ",max_n)
print("manimum no : ",min_n)
print("sum of all no : ",sum)



# How will you compare two lists?
# by == operator
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = [3, 2, 1]
# print(list1 == list2) 
# print(list1 == list3)




# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

def count_fun(lst):
    c = 0
    for i in lst:
        if len(lst)>=2 and i[0] == i[-1]:
            c = c+1
    return c

lst = ['python', 'programming', 'hello', 'madam', 'world', 'list']
print(count_fun(lst))



# Write a Python program to remove duplicates from a list.
def remove_duplicate(lst):
    return list(set(lst))
lst = [1,3,2,4,1,2,4,6,7,9,9]
print(remove_duplicate(lst))



# Write a Python program to check a list is empty or not.
def empty_check_fun(lst):
    if not lst:
        return True
    else:
        return False
lst1 = []
lst2 = [1,11,111]
print("is empty list : ",empty_check_fun(lst1))
print("is empty list : ",empty_check_fun(lst2))




# Write a Python function that takes two lists and returns true if they have at least one common member.
def myfun(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False
l1 = [1,2,3,56,78,90,12]
l2 = [43,67,54,32,78,22]
l3 = [87,99,87,65,45,67]
print(myfun(l1,l2))
print(myfun(l1,l3))




# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
def square_fun():
    s_lst = [x**2 for x in range(1,31)]
    f_five = s_lst[:5]
    l_five = s_lst[-5:]
    result_list = f_five + l_five
    return result_list
print(square_fun())



## Write a Python program to convert a list of characters into a string.
def covert_fun(lst):
    new_lst = ''.join(lst)
    return new_lst
lst = ['e','k','t','a',' ','m','o','l','i','y','a']
print(lst)
print(covert_fun(lst))




#  Write a Python program to select an item randomly from a list. 
import random
lst = [11,1,34,56,78,90,32,34,45,6,7,9,2,7]
print(random.choice(lst))




# Write a Python program to find the second smallest number in a list.
def myfun(lst):
    lst.sort()
    print("second smallest no : ",lst[1])
lst = [11,1,34,56,78,90,32,34,-1,45,6,7,9,2,7]
print(lst)
myfun(lst)




#  Write a Python program to check whether a list contains a sub list
def contain_sublist(lst,sub_lst):
    if sub_lst in lst:
        return True
    else:
        return False
lst1 = [1,2,3,4,[5,6,7],8,9,10]
s_lst = [5,6,7]
print(contain_sublist(lst1,s_lst))





# Write a Python program to split a list into different variables

my_list = [1, 2, 3, 4, 5]
a, b, c, d, e = my_list
print(a)  
print(b)  
print(c)  
print(d) 
print(e) 




#  What is tuple? Difference between list and tuple.
# tuple is a collection of data type which is immutable means once it is created, you can not modify its elements.
# it is sepearated by commas, and enclosed by parantheses ()
#Lists are defined using square brackets [], while tuples are defined using parentheses ().
# Example of a list
# my_list = [1, 2, 3, 4, 5]
# Example of a tuple
# my_tuple = (1, 'two', 3.0, [4, 5])




#Write a Python program to create a tuple with different data types.
#tuple = ('hello', 42, True, [1, 2, 3], {'a': 1, 'b': 2})
#print(tuple)


#  Write a Python program to create a tuple with numbers
# tuple = (1, 2, 3, 4, 5)
# print(tuple)



#  Write a Python program to convert a tuple to a string.
# tuple = ('h', 'e', 'l', 'l', 'o')
# string = ''.join(tuple)
# print(string)




# Write a Python program to check whether an element exists within a tuple. 
# tuple = ('apple', 'banana', 'cherry', 'orange')
# if 'banana' in tuple:
#     print('banana exists in the tuple')
# else:
#     print('banana does not exist in the tuple')



#  Write a Python program to convert a list to a tuple.
# list = ['apple', 'banana', 'cherry', 'orange']
# tuple = tuple(list)
# print('The tuple converted from the list is:',tuple)



# Write a Python program to reverse a tuple.
# tuple = (1, 2, 3, 4, 5)
# reversed_tuple = tuple[::-1]
# print( reversed_tuple)

#using reversed() method:
def rev_tuple(t):
    t_new = ()
    for i in reversed(t):
        t_new = t_new + (i,)
    print(t_new)
t1= ('e','k','t','a')
rev_tuple(t1)


"""













