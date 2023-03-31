

n= int(input("Enter no :"))

even_sum=0
odd_sum=0
for i in range(1,n+1):
    if i%2==0:
        print("even: ",i)
        even_sum = even_sum + i

    else:
        print("odd: ",i)
        odd_sum = odd_sum + i

print("sum of even no : ",even_sum)
print("sum of odd no : ",odd_sum)
