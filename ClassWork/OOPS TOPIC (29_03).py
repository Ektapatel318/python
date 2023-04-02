""" 
# class creation
class student:
     # data members in class (variables)
     name="Ekta"
     subject="python"
     technology="programming"
     # member function in class 
     # self:it represents current class properties
     def display(self):
         print("name= ",self.name)
         print("name= ",self.subject)
 # obj creation 
obj=student()
obj.display()




class faculty:
    # data members in class (variables)
     name="anjali"
     subject="python"
     
    # member function in class 
    # self:it represents current class properties
     def display(self):
         print("name= ",self.name)
         print("name= ",self.subject)
 # obj creation 
obj=faculty()
obj.display()

#-----------------------------------------------------------------------------------------

#create a class of person
class person:
    #method
    def display(self):          #self which is represent current class properties
        print("this is person method")
#object creation of class person
obj = person()
obj.display()

#-----------------------------------------------------------------------------------------
"""
# class define for student 
class student:
    # dictionary - we use as a database
    db = {}

    #input methood - which accept values from student user 
    def input_data(self):                # self keyword which is used to access inside class properties

        email = input("enter email : ")
        password = input("enter password : ")
        #storing data in db

        #here, email is key and password is value
        #e.g. e@gmail.com : 123456
        self.db[email] = password

    def display(self):
        #display alll students:
        for k in self.db.keys():
            print("email = ",k)

#object creation of student class 
s1 = student()

status = True
while status:
        
        s1.input_data()
        choice = input("do you want to add more students: ")
        if choice=='n':
             s1.display()






