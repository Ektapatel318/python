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
"""



    







