def to_hours(minutes):
    hours = minutes / 60
    return hours


result = to_hours(90)
print(f"{result} h")

result2 = to_hours(45)
print(f"45 min = {result2:.2f} h")

print(f"{to_hours(120):.2f}")