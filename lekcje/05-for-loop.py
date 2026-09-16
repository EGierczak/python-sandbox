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
