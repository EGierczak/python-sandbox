# sorted() returns a NEW list, the original stays unchanged
# to replace the original: numbers = sorted(numbers)

# reverse=True sorts from the largest down

# key takes a FUNCTION that says what to compare by
# the function name goes without parentheses: key=len, not key=len()

# lambda is a one-line function without a name
# lambda word: word[-1]  ->  takes word, returns its last letter
# no return needed, it returns automatically

# dict.items() gives pairs; in a pair, index 0 is the key, index 1 is the value
# key=lambda pair: pair[1]  ->  sort a dict by value, not by name

# two names after "for" unpack a pair into separate variables

minutes = [45, 120, 30, 90, 60]

sorted_list = sorted(minutes)
print(sorted_list)
print(minutes)
reversed_sorted_list = sorted(minutes, reverse=True)
print(reversed_sorted_list)

words = ["banana", "fig", "apple", "kiwi"]

print(sorted(words))
print(sorted(words, key=len))


def last_letter(word):
    return word[-1]


print(sorted(words, key=last_letter))

print(sorted(words, key=lambda word: word[-1]))

workouts = {"running": 45, "cycling": 90, "gym": 60, "walking": 30}
sorted_workouts = sorted(workouts.items(), key=lambda pair: pair[1], reverse=True)

for name, duration in sorted_workouts:
    print(f"{name}: {duration} min")
