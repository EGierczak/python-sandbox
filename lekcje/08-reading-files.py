# Lesson 08 — Reading files
#
# open("file.txt")   -> opens a file and gives a file object
# with ... as file:  -> the file is automatically closed when the block ends
#                       (keep only the reading inside the with-block)
# file.read()        -> reads the whole file as ONE string (str),
#                       so content[0] is the first character, not the first line
# .splitlines()      -> splits a string at line breaks and returns a list,
#                       one line = one element
# len(list)          -> number of elements in a list
#
# Relative paths start from the WORKING DIRECTORY, not from the .py file.
# PyCharm's Run button uses the script's folder -> "shopping.txt" works.
# Running from the project root in terminal would need "lekcje/shopping.txt".
#
# Data lives in the file: change the .txt, the program stays the same.

with open("shopping.txt") as file:
    content = file.read()

print(content)

print(type(content))
print(content[0])

products = content.splitlines()
print(products)
print(type(products))
print(products[0])

print("Shopping list:")
for product in products:
    print(f"- {product}")

print(f"Products on the list: {len(products)}")