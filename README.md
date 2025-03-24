upper() – Converts a string to uppercase

Example

text = "hello"
print(text.upper())  # Output: "HELLO"

lower() – Converts a string to lowercase

Example

text = "Hello WORLD"
print(text.lower())  # Output: "hello world"

capitalize() – Capitalizes the first letter of the string

text = "hello world"
print(text.capitalize())  # Output: "Hello world"

title() – Capitalizes the first letter of each word

text = "hello world"
print(text.title())  # Output: "Hello World"

swapcase() – Swaps uppercase letters to lowercase and vice versa

text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

find(substring) – Finds the first occurrence of a substring (returns -1 if not found)

text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1

index() - finds the index of the first occurrence of a specified substring within a string.

text = "Hello, world!"
index = text.index("world")
print(index)  # Output: 7

startswith(substring) – Checks if a string starts with a given substring

text = "hello world"
print(text.startswith("hello"))  # Output: True

endswith(substring) – Checks if a string ends with a given substring

text = "hello world"
print(text.endswith("world"))  # Output: True

count(substring) – Counts occurrences of a substring

text = "hello world, hello Python"
print(text.count("hello"))  # Output: 2

replace(old, new) - Replaces all occurrences of old with new in the string.

text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

strip() - Removes leading and trailing whitespace or specified characters.

text = "   hello world   "
print(text.strip())  # Output: "hello world"

lstrip() - Removes leading whitespace or specified characters from the string.

text = "   hello"
print(text.lstrip())  # Output: "hello"

rstrip() - Removes trailing whitespace or specified characters from the string.

text = "hello   "
print(text.rstrip())  # Output: "hello"

split(separator) - Splits the string into a list using the specified separator.

text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']
