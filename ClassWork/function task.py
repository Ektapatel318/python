def addition():
    n1 = int (input("enter no 1: "))
    n2 = int (input("enter no 2: "))
    ans = n1+n2
    print("addtion is : ",ans)

def mul():
    n1 = int (input("enter no 1: "))
    n2 = int (input("enter no 2: "))
    ans = n1*n2
    print("addtion is : ",ans)

def menu():
    data= """
            Menu :

            press 1 for addition
            press 2 for multiplication


          """
    print(data)
    choice = int(input("enter your choice : "))
    if choice == 1 :
            addition()

    elif choice == 2:
            mul()

menu()






 
