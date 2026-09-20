# A dictionary solves the problem of keeping two lists in sync: instead of searching by position, we search by name.
# A dictionary stores pairs: a key and a value assigned to that key. Keys are unique. Values can repeat and can be any type (number, string, list...).
# Reading by key gives us the value assigned to this key.
# KeyError means that the key does not exist.
# The same syntax is used to change and to add: dict[key] = value. If the key already exists, the value will be changed; if not, a new key with this value will be added.
# By default, a for loop over a dictionary gives only the keys. If we use dict.items(), we get each key-value pair.

workout = {"squats": 20, "push-ups": 15, "plank": 60}

print(workout["push-ups"])
print(workout["plank"])
#print(workout[0])

workout["plank"] = 50
print(workout["plank"])
workout["hip thrust"] = 50

print(workout)

for exercise in workout:
    print(f"{exercise}: {workout[exercise]}")

for exercise, reps in workout.items():
    print(f"{exercise}: {reps}")

prices = {"milk": 3.50, "bread": 6.79, "chocolate": 9.99}
print(prices)
prices["milk"] = 3.90
print(prices)
prices["butter"] = 5.00

for item, price in prices.items():
    print(f"{item}: {price:.2f} zł")














