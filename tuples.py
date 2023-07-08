# Tuples are immutable lists. Meaning that they cannot be changed
# Tuples are faster than lists because there is
# only tuple.count() and tuple.index()
# Tuples are used to protect data from being changed

foods = ('pizza', 'pasta', 'pizza', 'salad', 'soup', 'sandwich')
for food in foods:
    print(food)
    print("The count of", food, "is", foods.count(food))
    print("The index of", food, "is", foods.index(food))
