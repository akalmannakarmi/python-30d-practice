# Use filter to filter out countries having exactly six characters.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def remSL(name):
    if len(name) != 6:
        return True
    
NoSL_countries = filter(remSL,countries)
print(list(NoSL_countries))