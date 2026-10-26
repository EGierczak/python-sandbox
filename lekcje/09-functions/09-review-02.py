# Function writing practice after a break.
# def + argument + return.
# * keeps the type: int * int = int, but float * int = float.

def to_seconds(minutes):
    seconds = minutes * 60
    return seconds


print(f"5 minutes = {to_seconds(5)} seconds.")
print(f"0.5 minutes = {to_seconds(0.5):.0f} seconds.")
