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

# reverse() => Reverses the elements of the list in place.
<!-- Example -->
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# copy() => Returns a shallow copy of the list.
<!-- Example -->
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

# len(list) => Returns the number of elements in the list.
<!-- Example -->
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

# max(list) => Returns the maximum element in the list.
<!-- Example -->
my_list = [1, 2, 3]
print(max(my_list))  # Output: 3

# min(list) => Returns the minimum element in the list.
<!-- Example -->
my_list = [1, 2, 3]
print(min(my_list))  # Output: 1

# sum(list) => Returns the sum of all elements in the list.
<!-- Example -->
my_list = [1, 2, 3]
print(sum(my_list))  # Output: 6
my_list = [1, 2, 3]
print(sum(my_list))  # Output: 6

# Slicing: list[start:end:step] => Used to get a subset of the list.
<!-- Example -->
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])      # Output: [2, 3, 4]
print(my_list[::-1])     # Output: [5, 4, 3, 2, 1]

# del list[i] => Deletes the element at index i.
<!-- Example -->
my_list = [1, 2, 3]
del my_list[1]
print(my_list)  # Output: [1, 3]

# list1 + list2 => Concatenates two lists.
<!-- Example -->
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
