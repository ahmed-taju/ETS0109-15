LIST METHODES

# append(x) => Adds an item x to the end of the list.
<!-- Example -->
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# extend(iterable) => Adds all elements of an iterable (e.g., another list) to the end of the list.
<!-- Example -->
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # Output: [1, 2, 3, 4]

# insert(i, x) => Inserts an item x at a specific index i.
<!-- Example -->
my_list = [1, 3, 4]
my_list.insert(1, 2)
print(my_list)  # Output: [1, 2, 3, 4]

# remove(x) => Removes the first occurrence of the value x in the list.
<!-- Example -->
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# pop([i]) => Removes and returns the element at index i. If i is not provided, removes the last element.
<!-- Example -->
my_list = [1, 2, 3]
popped = my_list.pop(1)
print(my_list)  # Output: [1, 3]
print(popped)   # Output: 2

# clear() => Removes all elements from the list.
<!-- Example -->
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# index(x[, start[, end]]) => Returns the index of the first occurrence of x in the list within the optional start and end range.
<!-- Example -->
my_list = [1, 2, 3, 2]
print(my_list.index(2))  # Output: 1

# count(x) => Returns the number of times x appears in the list.
<!-- Example -->
my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))  # Output: 3

# sort(*, key=None, reverse=False) => Sorts the list in place. Use key for custom sorting and reverse=True for descending order.
<!-- Example -->
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

# Descending order
my_list.sort(reverse=True)
print(my_list)  # Output: [4, 3, 2, 1]

