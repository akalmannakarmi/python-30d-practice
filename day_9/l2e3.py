# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter Fruit: ")
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")