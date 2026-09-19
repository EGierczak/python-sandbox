# ===== Lesson 06: conditions =====

# Comparisons return a bool (True or False):
#   ==  equal          !=  not equal
#   >   greater        <   less
#   >=  greater/equal  <=  less/equal
# "=" assigns a value, "==" asks a question. In conditions I almost always want "==".

# if -> the body runs once or not at all (a loop body can run many times).
# Colon + indentation = the body, just like in a for loop.
# The first line without indentation always runs.

# if / elif / else:
# - Python checks the conditions from top to bottom
#   and runs ONLY the first branch that is True. The rest is skipped.
# - Order matters: put the narrowest condition first (>= 6 before >= 4 before >= 1),
#   otherwise a wide condition "eats" the narrow ones.
# - else has no condition. It catches everything that didn't match.
# - An empty list has len() == 0, so it lands in else.
#   Always ask: "what happens when the list is empty?"

# Combining conditions:
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips True to False and False to True
# "and" is evaluated before "or" (like * before +).
# Method: solve each comparison to True/False first, then combine.

# TRAP: day == "Saturday" or "Sunday"
# Python does NOT repeat "day ==". "Sunday" alone is a non-empty string,
# so it always counts as True, and the whole condition is always True.
# Fix: repeat the comparison, or store the answer in a bool:
#   is_weekend = day == "Saturday" or day == "Sunday"
# Names starting with "is_" are a convention for bools. They read like a question.

# Each elif already "knows" that every condition above it was False.

# Case sensitivity: "saturday" == "Saturday" is False.
# No error, just a silent wrong result ("Weekday training" on a Saturday).
# Fix comes in lesson 08 with .lower().

exercises = ["squat", "deadlift", "bench press", "hip thrust", "hip thrust", "hip thrust"]

if len(exercises) >= 6:
    print("Heavy day")
elif len(exercises) >= 4:
    print("Long workout today")
elif len(exercises) >= 1:
    print("Short workout today")
else:
    print("Rest day")
print("Let's go")

day = input("What day is it today?: ")
number_of_exercises = int(input("How many exercises do you want to do today?: "))
is_weekend = day == "Saturday" or day == "Sunday"

if is_weekend and number_of_exercises >= 4:
    print("Long weekend session")
elif is_weekend:
    print("Easy weekend")
elif not is_weekend and number_of_exercises == 0:
    print("Rest day")
else:
    print("Weekday training")