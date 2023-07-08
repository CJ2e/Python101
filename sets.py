# sets look alot like a dictionary, but they are not
# sets are used to remove duplicates from a list
# They also have no particular order and cannot be accessed by index

lst = [1, 2, 3, 4, 5, 5]
dictionary = {"key": "value", "key2": "value2"}
set = {1, 2, 3, 4, 5, 5}
print("List:", lst)
print("Dictionary:", dictionary)
set.remove(3)
set.add(6)
print("Set:", set)
