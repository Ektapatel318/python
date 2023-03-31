"""
we can create, read and write file using of python 

there are 4 modes in python file handling 

r : read mode
w : write mode
x : create mode 
a : append mode




#take one variable which open file
f = open("myfile.txt","r")
print(f.read())

#other method to open file
with open("myfile.txt","r") as f:
print(f.read())

#---------------------------------------------------------

#open any file in specific variable
f = open("mynewfile_file.txt","w")   # w - write mode

#accept value from user 
name = input("enter name: ")

#using of write() write file
f.write("\n"+name)

#close file 
f.close()


#---------------------------------------------------------

#open any file in specific variable
f = open("mynewfile_file.txt","a")   # a - append mode

#accept value from user 
name = input("enter name: ")

#using of write() write file
f.write("\n"+name)

#close file 
f.close()

"""

#---------------------------------------------------------
#create a blank file
f = open("blankfile.txt","x")
f.close()


