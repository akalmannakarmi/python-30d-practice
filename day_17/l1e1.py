# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

nordic_countries = [names.pop(0) for i in range(5)]
es = names.pop(0)
ru = names.pop(0)

print(nordic_countries)
print(es)
print(ru)