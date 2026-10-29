def read_numbers(filename):
    with open(filename) as file:
        content = file.read()
        lines = content.splitlines()

    numbers = []

    for minutes in lines:
        numbers.append(int(minutes))

    return numbers


result = read_numbers("minutes.txt")
print(result)
