with open("minutes.txt") as file:
    content = file.read()

lines = content.splitlines()

total = 0
for line in lines:
    minutes = int(line)
    total = total + minutes

print(f"Total training time: {total} minutes")