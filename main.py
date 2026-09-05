text = "kot pies kot mysz kot pies kot"
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

ranking = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

for word, count in ranking[:5]:
    print(f"{word}: {count}")