# Lesson 05 — for loop
#
# Problem: printing list items by index (exercises[0], [1]...) breaks
# when the list grows — the number of repetitions is hardcoded. A loop is the solution.
#
# for item in items:
#     do something with item
#
# The loop runs once for each item. The number of passes equals the number of items in the list.
# - "item" is a new variable, holds the next element on each pass
# - colon (:) starts the loop body
# - indentation (4 spaces) = loop body
# - first unindented line runs once, after the loop ends
# - no indexes, no IndexError, works for any list length
# - naming convention: plural list, singular item (exercises / exercise)

# enumerate(items, start=1) — gives pairs (number, item), one per pass
# - two names after "for" because each pass delivers two values
# - order comes from the pair, not from the line: number first, item second
# - start=1 is an argument of the function, not a property of the list
#
# slicing — items[start:end] returns a NEW LIST, not a single item
# - start is included, end is not: items[1:4] gives indexes 1, 2, 3
# - shortcuts: items[:3] from the beginning, items[3:] to the end, items[-2:] last two
#
# a loop variable stays alive after the loop ends, holding the last element
# - a typo in the "for" line can silently print that old value, with no error


exercises = ["squat", "bench press", "deadlift", "hip thrust", "crunches"]

for exercise in exercises:
    print(f"Next exercise: {exercise}")
print(f"Done! Total: {len(exercises)} exercises")

# --- Practice from scratch ---

groceries = ["milk", "chips", "water", "fish"]
for grocery in groceries:
    print(f"- {grocery}")
print(f"First item: {groceries[0]}, last item: {groceries[-1]}")
print(f"You need to buy {len(groceries)} items")


for number, exercise in enumerate(exercises, start=1):
    print(f"{number}. {exercise}")

# --- slicing ---

print("Warm-up:")
for exercise in exercises[:3]:
    print(f"- {exercise}")
print("Main part:")
for exercise in exercises[3:]:
    print(f"- {exercise}")