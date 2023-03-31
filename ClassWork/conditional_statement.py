"""
conditional statement

"""

"""
program : 1

no = int(input("Enter any no."))

if no>0:
    print("\nit is +ve")
else:
    print("\nit is -ve")


program : 2

no1= int(input("Enter no 1 : "))
no2= int(input("Enter no 2 : "))
no3= int(input("Enter no 3 : "))

print("no 1: ",no1 "no 2: ",no2 "no 3: ",no3)
if no1>no2:
    if no1>no3:
        print(no1," is greater")

    else:
        print(no3," is greater")
else:
    if no2>no3:
        print(no2," is greater")
    else:
        print(no3," is greater")

"""

"""
program : 3 ladder if/else
"""

roll_no = int(input("enter your roll no :"))
name = input("enter your name :")
m = int(input("enter maths marks :"))
p = int(input("enter physics marks :"))
c = int(input("enter chemistry marks :"))

total = m+p+c
per = (total)/3

print("-"*90)
print()
print("roll no: ",roll_no)
print("name : ",name)
print("total marks : ",total)
print("percentage : ",per)

if per>=70:
    print("class is distinction")

elif per>=60:
    print("first class")

elif per>=50:
    print("second class")

elif per>=40:
    print("Pass Class")

else:
    print("fail")


    
























