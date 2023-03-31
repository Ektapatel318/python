
"""
#exception handling code 
try:
      print(a)
except:
      print("variable declaration is not done")

#----------------------------------------------------------
try:
    #accept numbers from user
    n1= int(input("enter no 1:"))
    n2= int(input("enter no 2:"))
    ans= n1/n2
    print(ans)

except:
    print("Invalid input")

#----------------------------------------------------------
try: 
    n1= int(input("enter no 1:"))
    n2= int(input("enter no 2:"))

    ans = n1/n2
    print(ans)

except ValueError:
    print("invalid input - only 0-9 required")
except ZeroDivisionError:
    print("cannot divided by zero")
except:
    print("invalid output")


#----------------------------------------------------------

#list define 
l1 = [10,20,403,50,60,70]

try:
    #acceess specific element from the list
    print(l1[2])
except:
    print("list index out of bound")
else:
    #display list
    print(l1)


#--------------------------------------------------------
try:
    print(a)
except Exception as e:
    print(e)


#--------------------------------------------------------

#import sys module
import sys

#exception handling block 
try:
    print(a)
except:
    print("subject = ",sys.exc_info()[0])
    print("message = ",sys.exc_info()[1])

"""
#----------------------------------------------------------













    