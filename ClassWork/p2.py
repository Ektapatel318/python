
db = {}

def registration(firstname,email,password):
    db['name']= firstname
    db['email']=email
    db['password'] = password
    print("Registration successfully")

def login(email,passoword):

    if email == db['email']:
        if password == db['password']:
            return db['name']
        else:
            return "invalide email or password "
    else:
        return "invalid email or password"
    
    status true
    while status:
            menu = """
            
                    1) PRESS 1 for registration 
                    2) PRESS 2 for login
                    3) press 3 for exit
                
                """
            
        print(menu)

        if choice == 1:

            name= input("enter your name")
            email = input("enter your mail")
            password = input("enter your password")

            registration(name,email,password)
            
        elif choice == 2:
            email= input("enter your email")
            password=input("enter your password")
            print(login(email,password))

        elif:
            status = false
            



            





