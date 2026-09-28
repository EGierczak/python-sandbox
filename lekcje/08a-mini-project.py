# Lesson 08a: review mini-project (grocery receipt)
# Reads a shopping list from groceries.txt, looks up prices in a dictionary,
# prints a receipt, the total and a budget check.
#
# Takeaways:
# - Loop over the lines from the file, not over the prices dict.
#   The file decides what is on the receipt; the dict is only a price list.
# - Names in the file must match the dict keys exactly, otherwise KeyError.
# - Proof that the file is really used: change only the data, and the result changes.
# - Always format money with :.2f (floats are not exact).
# - Counter (total = 0) goes right above the loop, the result is printed once after it.
#
# Style (PEP 8):
# - One blank line between logical parts of the program.
# - Spaces around = and operators, after commas and after : in a dict.
# - No spaces inside brackets or before ( of a function call.

with open("groceries.txt") as file:
    content = file.read()

lines = content.splitlines()

prices = {"milk": 3.99, "bread": 6.89, "cookies": 4.20, "honey": 15.75, "pasta": 8.99, "rice": 2.49}
budget = 30

total = 0
for line in lines:
    if prices[line] > 10:
        print(f"{line}: {prices[line]:.2f} zł (expensive)")
    else:
        print(f"{line}: {prices[line]:.2f} zł")
    total += prices[line]

print(f"Total: {total:.2f} zł")

if total > budget:
    print(f"Over budget by {total - budget:.2f} zł")
else:
    print(f"Within budget, {budget - total:.2f} zł left")
