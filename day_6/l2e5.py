# Slice out the first three items and the last three items from food_staff_lt list
fruits = ("fruit1","fruit2")
vegetables = ("vegetable1","vegetable2")
animal_products = ("animal_product1","animal_product2")
food_stuff_tp = fruits+vegetables+animal_products
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])