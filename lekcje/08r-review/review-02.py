with open("review.txt") as file:
    content = file.read()
lines = content.splitlines()
for number, line in enumerate(lines, start=1):
    print(f"{number}. {line}")