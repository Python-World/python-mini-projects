import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

password = "".join(random.choices(total, k=length))

print(password)
