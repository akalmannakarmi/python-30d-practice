# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

countries = [{'country':item[0][0],'city':item[0][1]} for item in countries]
print(countries)