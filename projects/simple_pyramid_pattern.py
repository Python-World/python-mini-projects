# A program to make a simple pyramid pattern

def pattern(n):
  k = 2 * n - 2
  
  # first for loop for every iteration of a row
  
  for i in range(0,n):
    
  # first nested for loop
  # for correct spaces
  
    for j in range(0,k):
      print(end = " ")
      
    k = k - 1 # decrementation of k (spaces)
    
  # second nested loop
  # for printing correct asterisk (*)
  
    for j in range(0,i + 1):
      print("* ",end = "")
    print("\r")
    
while True:
  try:
    a = "Enter a Positive Integer\n"
    b = "that's value has to be above 2 : "
    n = int(input(a + b))
    print("\n")

    if n <= 2:
      print("Please enter a valid Integer !")
    else:
      pattern(n)
      print("\n")
  except:
    print("Enter a valid Integer")
