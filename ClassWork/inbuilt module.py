"""
import instaloader

name = input("enter instagram username: ")
insta = instaloader.Instaloader()
insta.download_profile(name,profile_pic__only=True)




from datetime import date
mydate = date(2023,3,12)
print("date :",mydate)

from datetime import date
current_date = date.today()


print("current date = ",current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)



from datetime import time
#t= time(10,20,45)
#print(t)
"""
import platform

print(platform.architecture())
print(platform.python_version())
print(platform.machine())
print(platform.processor())



