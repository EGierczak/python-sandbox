# print vs return:
# - print only shows a value on the screen; it can't be used later
# - return hands the value back to the caller; store it in a variable
#   (or print it), otherwise it's lost
# - a function without return gives back None

# Naming:
# - functions = verbs, they do something (read_lines, count_exercises)
# - variables = nouns, they store something (exercises, lines)
# - don't reuse a function's name for a variable:
#   exercises = exercises(...) replaces the function with a list

def read_lines(filename):
    with open(filename) as file:
        content = file.read()
        lines = content.splitlines()

    return lines

exercises = read_lines("workouts.txt")
print(exercises)
print(f"List contains: {len(exercises)} exercises")

sorted_exercises = sorted(exercises)

for number, exercise in enumerate(sorted_exercises, start=1):
    print(f"{number}. {exercise}")
