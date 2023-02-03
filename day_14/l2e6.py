# Use filter to filter out countries containing six letters and more in the country list.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def remL(name):
    if len(name) < 6:
        return True
    
NoL_countries = filter(remL,countries)
print(list(NoL_countries))