# user defined exception
# create class which inheriate exception 

# user defined exception 
class OddException(Exception):
    pass

#----------------------------------
#main program execution 

#accept value from user
n = int(input("Enter num: "))

try:
    #check condition
    if n%2==0:
        print("even no")
    else:
        #raise Exception
        raise Exception
except:
    print("odd num is not allowed")


#--------------------------------------------------------------------------------------------------




 