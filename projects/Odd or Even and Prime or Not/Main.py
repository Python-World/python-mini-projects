

'''
Name: Prajwal Kedari
Country:India
GitHub: prajwalkedari , prajwal-kedari
Link: https://www.github.com/prajwalkedari/
Source: Python-world
Thank!!!
'''

num = int(input("Enter a number: "))
if (num % 2) == 0:
   Odd_or_even_result=f"{num} is Even as well as"
else:
   Odd_or_even_result=f"{num} is Odd as well as"
if num > 1: 
    for i in range(2, int(num/2)+1): 
        if (num % i) == 0: 
            prime_or_not_result=" nor  prime number" 
            break
    else: 
        prime_or_not_result=" prime number"
else: 
    prime_or_not_result=" nor prime number"

print(Odd_or_even,prime_or_not_result)
