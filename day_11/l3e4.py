# Write a function which check if provided variable is a valid python variable

def valid_variable(var):
    var = ""
    if var.isidentifier() or var[0].isnumeric():
        return False
    for v in var:
        if v in '-?#':
            return False
    return True