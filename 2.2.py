ids = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input2.txt", "r") as input:
    for line in input:
        ids.append(line[:-1])

for a in ids:
    for b in ids:
        countsame = 0
        for i in range (0, len(a)):
            if a[i] != b[i]:
                countsame += 1
        if countsame == 1:
            print(a, b)
            break