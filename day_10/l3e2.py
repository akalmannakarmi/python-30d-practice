# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

mylist = ['banana', 'orange', 'mango', 'lemon']

for i in range(0,int(len(mylist)/2)):
    t = mylist[i]
    mylist[i] = mylist[-(i+1)]
    mylist[-(i+1)] = t
    
print(mylist)