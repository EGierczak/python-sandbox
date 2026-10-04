exercises = ["bench press", "pull up", "squat"]
print(f"Today's plan: {len(exercises)} exercises")
exercises.append(input("Add another exercise: "))
print(f"Your first exercise is: {exercises[0]}. Your last exercise is: {exercises[-1]}")
print(f"Your exercise list: {exercises}, number of exercises: {len(exercises)}")


#Notes
#Indexes start from 0, so the last index is len(list) - 1
#Negative indexes cont from the end: exercises[-1] is the last one
#len(exercises) - function, returns number of elements
#exercises.append("value") - method, adds value at the end of the list
#exercises.remove("value") - method, removes the FIRST element with this value
#exercises[1] = "value" - replaces element at position 1 (works on index, not value)
#Lists allow duplicates - append twice, get two elements
#IndexError - the index I'm trying to refer to doesn't exist
#ValueError - remove() got a value that is not in the list