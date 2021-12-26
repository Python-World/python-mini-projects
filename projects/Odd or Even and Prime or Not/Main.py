

'''
Name: Prajwal Kedari
Country:India
GitHub: prajwalkedari , prajwal-kedari
Link: https://www.github.com/prajwalkedari/
Source: Python-world
Thank!!!
''''

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(f"{num} is Even")
else:
   print(f"{num} is Odd")
if num > 1: 
    for i in range(2, int(num/2)+1): 
        if (num % i) == 0: 
            print(num, "is not a prime number") 
            break
    else: 
        print(num, "is a prime number") 
else: 
    print(num, "is not a prime number")
