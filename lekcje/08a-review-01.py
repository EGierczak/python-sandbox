# Zadanie 1
minutes = [20, 45, 0, 90, 30]
for minute in minutes:
    if minute == 0:
        print(f"{minute} min: no session")
    elif minute < 30:
        print(f"{minute} min: short session")
    else:
        print(f"{minute} min: long session")

# Zadanie 2
stock = {"milk": 2, "bread": 0, "eggs": 6}
stock["apple"] = 3
stock["milk"] = 1
for item in stock:
    print(f"{item}: {stock[item]}")
    if stock[item] == 0:
        print(f"Buy {item}")

# Zadanie 3
with open("review.txt") as file:
    content = file.read()

lines = content.splitlines()
print(f"Lines counter: {len(lines)}")
print(f"First line: {lines[0]}")
print(f"Last line: {lines[-1]}")
