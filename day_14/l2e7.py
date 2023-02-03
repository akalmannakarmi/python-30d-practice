# Use filter to filter out countries starting with an 'E'

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def remE(name):
    if not name.startswith('E'):
        return True
    
NoE_countries = filter(remE,countries)
print(list(NoE_countries))