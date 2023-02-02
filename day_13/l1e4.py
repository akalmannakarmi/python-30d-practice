# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[item[0][0],item[0][0][:3].upper(),item[0][1]] for item in countries]

print(countries)