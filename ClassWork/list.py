
l = [1,2,2.2,3.2,4,True,0,"ekta",0,"moliya"]

print(l)

l.append(80)
print(l)

l1=l.copy()
print(l1)

l2=l1.copy()
print(l2)

l1.append(90)
print(l1)

l2.append(100)
print(l2)

print(l.count(0))
print(l.count(1))

#l.pop()
#print(l)


l3 = [1001,1002,1003]
l.extend(l3)
print(l)

print(l.index(1001))

l.insert(6,"Tops")
print(l)

l.remove(1001)
print(l)

#l.reverse()
#print(l)

for i in l:
    print(i)
