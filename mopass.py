import numbers
import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
m1 = list(string.digits)
m2 = list(string.punctuation)

num = input("Enter Number Of Password : ")

while True:
    try:
        num = int(num)
        if num < 9 :
            print("Please Enter Number From 9 To 50 ")
            num = input("Enter Number Of Password Again : ")
        elif num > 50 :
            print("Please Enter Number From 9 To 50 ")
            num = input("Enter Number Of Password Again : ")
        else:
            break
    except:
        print("Please Enter Correct Number From 9 To 50 ")
        num = input("Enter Correct Number Of Password Again :")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(m1)
random.shuffle(m2)

p1 = round(num*(30/100))
p2 = round(num*(20/100))

password = []
for i in range(p1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(p2):
    password.append(m1[i])
    password.append(m2[i])

random.shuffle(password)

password = "".join(password[0:]) 

print(password)