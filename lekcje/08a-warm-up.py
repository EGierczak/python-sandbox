with open("tasks.txt") as file:
    content = file.read()

lines = content.splitlines()

for line in lines:
    print(f"- {line}")

print(f"Total: {len(lines)} tasks")