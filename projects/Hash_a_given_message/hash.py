import hashlib
def has():
    print("Available algorithms are: ")
    q=sorted(list(hashlib.algorithms_available))
    for i in range(len(q)):
        print('{0: <20}'.format(q[i]),end="")
        if i%3==2:
            print()
    str2hash = list(input("Enter the names of the algorithms separated by space : ").split())
    stri=input("Enter the message: ")
    for i in str2hash:
        i=i.lower()
        if i in list(hashlib.algorithms_available):
            result = hashlib.new(i)
            result.update(stri.encode())
            print("The hexadecimal equivalent of "+i+" hash is : ", end ="") 
            print(result.hexdigest())
        else:
            print(i+" is not a valid algorithm name")


print("------Secure messages with hash--------")
has()
inp=input("Do you wish to continue?[y/n]")
while inp.lower()=='y':
    has()
    inp=input("Do you wish to continue?[y/n]")
print("Goodbye")



