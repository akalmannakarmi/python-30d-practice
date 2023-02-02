# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

from string import ascii_letters as letters,digits
from random import choice

def random_user_id():
    result=[]
    valid = letters+digits
    keySize = int(input("Size of keys:"))
    no_keys = int(input("How many keys:"))
    for i in range(no_keys):
        t=''
        for i in range(keySize):
            t+=choice(valid)
        result.append(t)
    return result

print(random_user_id())