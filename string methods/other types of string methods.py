# f-strings (f"...") - Formats strings directly using variables or expressions inside curly braces.

# Example

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."

# len(obj) - Returns the length of the string (or other iterable).

# Example

text = "hello"
print(len(text))  # Output: 5

# encode(encoding) - Encodes the string into bytes using the specified encoding.

# Example

text = "hello"
print(text.encode('utf-8'))  # Output: b'hello'

# str.islower() - Checks if all alphabetic characters in the string are lowercase.

# Example

text = "hello"
print(text.islower())  # Output: True

# str.isupper() - Checks if all alphabetic characters in the string are uppercase.

# Example

text = "HELLO"
print(text.isupper())  # Output: True
