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

# dict.setdefault(key, default) => Returns the value of key. If not present, inserts key with a value of default.
<!-- Example -->
my_dict = {"a": 1}
my_dict.setdefault("b", 2)
print(my_dict)  # Output: {'a': 1, 'b': 2}

# dict.update(other_dict) => Updates the dictionary with key-value pairs from another dictionary.
<!-- Example -->
my_dict = {"a": 1}
my_dict.update({"b": 2, "c": 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# dict.values() => Returns a view object of dictionary values.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
print(my_dict.values())  # Output: dict_values([1, 2])

# dict.fromkeys(seq, value=None) => Creates a new dictionary from a sequence of keys with a specified value.
<!-- Example -->
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# dict.__contains__(key) => Returns True if the dictionary contains the specified key. This is usually accessed using the in keyword.
<!-- Example -->
my_dict = {"a": 1}
print("a" in my_dict)            # Output: True
print(my_dict.__contains__("a"))  # Output: True

# dict.__len__() => Returns the number of items in the dictionary.
<!-- Example -->
my_dict = {"a": 1, "b": 2}
print(len(my_dict))           # Output: 2
print(my_dict.__len__())      # Output: 2
