with open("tasks.txt") as file:
    content = file.read()

tasks = content.splitlines()

print("Today:")
for task in tasks:
    print(f"* {task}")

print(f"Tasks: {len(tasks)}")