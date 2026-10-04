def to_hours(minutes):
    return minutes / 60


result = to_hours(120)
print(result)
print(f"90 minutes = {to_hours(90)} hours")


def to_minutes(hours):
    return hours * 60


result = to_minutes(1.5)
print(result)
print(f"2 hours = {to_minutes(2)} minutes")