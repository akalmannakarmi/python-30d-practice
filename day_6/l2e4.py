# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
fruits = ("fruit1","fruit2")
vegetables = ("vegetable1","vegetable2")
animal_products = ("animal_product1","animal_product2")
food_stuff_tp = fruits+vegetables+animal_products
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_tp[int(len(food_stuff_tp)/2)])
print(food_stuff_lt[int(len(food_stuff_lt)/2)])