Tuple methods in Python

# tuple.count(value) => Returns the number of times value appears in the tuple.
<!-- Example -->
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))  # Output: 3

# tuple.index(value, start=0, stop=len(tuple)) => Returns the index of the first occurrence of value.
<!-- Example -->
t = (10, 20, 30, 20, 40)
print(t.index(20))       # Output: 1
print(t.index(20, 2))    # Output: 3

# len(tuple) => Returns the number of items in the tuple.
<!-- Example -->
t = (1, 2, 3)
print(len(t))  # Output: 3

