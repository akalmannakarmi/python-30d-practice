# Writ a function which generates a six digit/character random_user_id.
from string import ascii_letters as letters,digits
from random import choice

def random_user_id():
    result=''
    valid = letters+digits
    for i in range(6):
        result+=choice(valid)
    return result

print(random_user_id())