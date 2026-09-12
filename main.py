with open("sample.txt") as file:
    text = file.read()

words = text.lower().split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

ranking = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

for word, count in ranking[:5]:
    print(f"{word}: {count}")