# Use map to change each name to uppercase in the names list

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def toUpper(s):
    return s.upper()

U_names=map(toUpper,names)
print(list(U_names))