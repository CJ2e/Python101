lst = [True, 1, 3.14, [1.1, 2, 3, 4], "Ciaran"]
lst.append("New Item")
popLastItem = lst.pop()  # this should store the appended item in popLastItem
for item in lst:
    print("The item is:", item)
print("The popped item is:", popLastItem)
