DICTIONARY

# dict.clear() => Removes all items from the dictionary.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
my_dict.clear()
print(my_dict)  # Output: {}

# dict.copy() => Returns a shallow copy of the dictionary.
<!-- Example -->
original = {"a": 1, "b": 2}
copy_dict = original.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}

# dict.get(key, default=None) => Returns the value for key if key is in the dictionary, else returns default.
<!-- Example -->
person = {"name": "Alice"}
print(person.get("name"))      # Output: Alice
print(person.get("age", 25))   # Output: 25

# dict.items() => Returns a view object of dictionary’s key-value pairs.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

# dict.keys() => Returns a view object of dictionary keys.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

# dict.pop(key, default) => Removes and returns the value of the specified key.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
value = my_dict.pop("a")
print(value)     # Output: 1
print(my_dict)   # Output: {'b': 2}
