# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def remE(name):
    if not name.startswith('E'):
        return True
def remLand(name):
    if name.find('land') == -1:
        return True
    
NoE_NoLand_countries = filter(remLand,filter(remE,countries))
print(list(NoE_NoLand_countries))