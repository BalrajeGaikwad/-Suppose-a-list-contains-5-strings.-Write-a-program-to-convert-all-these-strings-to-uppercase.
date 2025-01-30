"""
 Suppose a list contains 5 strings. Write a program to convert all these strings to uppercase.

"""

# List of 5 strings
words = ["apple", "banana", "cherry", "date", "elderberry"]


for i in range(len(words)):
    words[i]=words[i].upper()
print(words)