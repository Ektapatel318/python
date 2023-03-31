"""
string slicing

"""

s= "Tops Technologies"
print(s)

#positive values:
print(s[1:10])
print(s[:14])
print(s[6:])
print(s[1:13:2])
print(s[::4])

#negative values:

print(s[-17:-1])
print(s[-17:0]) #it will not give any output
print(s[:-6])
print(s[-5:])
print(s[-15:-2:2])
print(s[-1::-1])
