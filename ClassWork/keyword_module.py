import keyword
keyword_list = keyword.kwlist
name = input("enter nsame: ")
if name in keyword_list: 
    print("yes, it is keyword!")
else:
    print("no, it is not keyword!")

