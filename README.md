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

