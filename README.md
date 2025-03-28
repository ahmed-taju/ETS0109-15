# upper() – Converts a string to uppercase

<!-- Example -->

text = "hello"
print(text.upper())  # Output: "HELLO"

# lower() – Converts a string to lowercase

<!-- Example -->

text = "Hello WORLD"
print(text.lower())  # Output: "hello world"

# capitalize() – Capitalizes the first letter of the string

<!-- Example -->

text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# title() – Capitalizes the first letter of each word

<!-- Example -->

text = "hello world"
print(text.title())  # Output: "Hello World"

# swapcase() – Swaps uppercase letters to lowercase and vice versa

<!-- Example -->

text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

# find(substring) – Finds the first occurrence of a substring (returns -1 if not found) -->
 
 <!-- Example -->

text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1

# index() - finds the index of the first occurrence of a specified substring within a string.

<!-- Example -->

text = "Hello, world!"
index = text.index("world")
print(index)  # Output: 7

# startswith(substring) – Checks if a string starts with a given substring

<!-- Example -->

text = "hello world"
print(text.startswith("hello"))  # Output: True

# endswith(substring) – Checks if a string ends with a given substring

<!-- Example -->

text = "hello world"
print(text.endswith("world"))  # Output: True

# count(substring) – Counts occurrences of a substring

<!-- Example -->

text = "hello world, hello Python"
print(text.count("hello"))  # Output: 2

# replace(old, new) - Replaces all occurrences of old with new in the string.

<!-- Example -->

text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

# strip() - Removes leading and trailing whitespace or specified characters.

<!-- Example -->

text = "   hello world   "
print(text.strip())  # Output: "hello world"

# lstrip() - Removes leading whitespace or specified characters from the string.

<!-- Example -->

text = "   hello"
print(text.lstrip())  # Output: "hello"

# rstrip() - Removes trailing whitespace or specified characters from the string.

<!-- Example -->

text = "hello   "
print(text.rstrip())  # Output: "hello"

# split(separator) - Splits the string into a list using the specified separator.

<!-- Example -->

text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']

# join(iterable) - Joins elements of an iterable into a single string using the string as a separator.

<!-- Example -->

words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

# isalpha() - Checks if the string contains only alphabetic characters.

<!-- Example -->

text = "Hello"
print(text.isalpha())  # Output: True

# isdigit() - Checks if the string contains only numeric characters.

<!-- Example -->

text = "12345"
print(text.isdigit())  # Output: True

# isalnum() - Checks if the string contains only alphanumeric characters (letters and digits).

<!-- Example -->

text = "Hello123"
print(text.isalnum())  # Output: True

# isspace() - Checks if the string contains only whitespace characters.

<!-- Example -->

text = "   "
print(text.isspace())  # Output: True

# format(*args, **kwargs) - Formats the string with placeholders using provided arguments.

<!-- Example -->

text = "My name is {} and I am {} years old."
print(text.format("Alice", 25))  # Output: "My name is Alice and I am 25 years old."

# f-strings (f"...") - Formats strings directly using variables or expressions inside curly braces.

<!-- Example -->

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."

# len(obj) - Returns the length of the string (or other iterable).

<!-- Example -->

text = "hello"
print(len(text))  # Output: 5

# encode(encoding) - Encodes the string into bytes using the specified encoding.

<!-- Example -->

text = "hello"
print(text.encode('utf-8'))  # Output: b'hello'

# str.islower() - Checks if all alphabetic characters in the string are lowercase.

<!-- Example -->

text = "hello"
print(text.islower())  # Output: True

# str.isupper() - Checks if all alphabetic characters in the string are uppercase.

<!-- Example -->

text = "HELLO"
print(text.isupper())  # Output: True

