print("-----------Calculator----------")

#-------inputs
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operation = input("Choose: \nAdd(+) \nSubract(-) \nDivision(/) \nMultiplication(*) ")

#-------conditions
if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '/':
    print(num1 / num2)
    
elif operation == '*':
    print(num1 * num2)

else :
    print("You have selected other things!")