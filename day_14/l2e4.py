# Use filter to filter out countries containing 'land'.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def remLand(name):
    if name.find('land') == -1:
        return True

NoLand_countries=filter(remLand,countries)
print(list(NoLand_countries))