1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
import string
import random
 
print("+++Password Generator+++")
 
mxchars = string.ascii_letters+string.digits+string.punctuation
 
numInput = int(input("Enter the Number of passwords to Generate: "))
length = int(input("Enter the Password Length: "))
print("+++++++++++++++++++++++++++++++++++++++++++")
print("+++++++List(s) Generated Password:++++++++ ")
print("+++++++++++++++++++++++++++++++++++++++++++")
for pwd in range(numInput):
pw = ''
for c in range(length):
pw += random.choice(mxchars)
print(pw)