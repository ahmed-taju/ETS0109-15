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