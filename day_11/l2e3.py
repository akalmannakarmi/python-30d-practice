# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(data):
    if not data:
        return True
    return False

print(is_empty({}))