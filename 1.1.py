changes = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input1.txt", "r") as input:
    for line in input:
        changes.append(int(line))

frequency = 0
count = 0

seen_freqs = []

while (frequency not in seen_freqs):
    seen_freqs.append(frequency)
    frequency += changes[count % len(changes)]
    count += 1
    if (count % 1000 == 0):
        print(str(count), str(frequency))

print(frequency)