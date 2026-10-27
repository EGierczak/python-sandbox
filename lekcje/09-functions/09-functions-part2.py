def sum_minutes(filename):
    with open(filename) as file:
        content = file.read()
        lines = content.splitlines()

    total = 0

    for line in lines:
        total = total + int(line)

    return total


first = sum_minutes("minutes.txt")
print(f"Total: {first} minutes")

second = sum_minutes("minutes2.txt")
print(f"Total: {second} minutes")