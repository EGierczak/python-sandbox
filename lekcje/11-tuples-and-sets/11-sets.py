# Lesson 11 part 2: sets
#
# set = a collection where every element appears at most once
# set(my_list) turns a list into a set - duplicates disappear
# a set has no order: no indexes (my_set[0] does not work)
#   and the print order can change between runs
# len() and "in" work the same as with a list
#
# loop version (same result, more code):
#   empty list -> for loop -> if x not in the list -> append
#
# my mistake: "is not" vs "not in"
#   x not in my_list -> is x NOT inside the list? (what I wanted)
#   x is not my_list -> is x NOT the same object as the list? (always True here)
#   no error, just a wrong result - all duplicates got added
#
# list -> when order or repeats matter
# set  -> when I only care which elements are there

def read_lines(filename):
    with open(filename) as file:
        content = file.read()
        lines = content.splitlines()
        return lines


workouts = read_lines("workouts.txt")

print(workouts)
print(f"Entries: {len(workouts)}")

unique_exercises = []

for exercise in workouts:
    if exercise not in unique_exercises:
        unique_exercises.append(exercise)

print(unique_exercises)
print(f"Unique: {len(unique_exercises)}")

exercise_set = set(workouts)
print(exercise_set)
print(f"Unique (set): {len(exercise_set)}.")