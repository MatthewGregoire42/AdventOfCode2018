# Input parsing and representation

data = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input25.txt", "r") as input:
    for line in input:
        data.append([int(a) for a in line[:-1].split(",")])

constellations = []

constellations.append([data[0]])
del data[0]

b = 0

while data:
    a = 0
    hist = len(data)
    while a < len(data):
        for c in constellations[b]:
            if a < len(data):
                p = data[a]
                dist = abs(c[0]-p[0]) + abs(c[1]-p[1]) + abs(c[2]-p[2]) + abs(c[3]-p[3])
                if dist <= 3:
                    constellations[b].append(p)
                    data.remove(p)
        a += 1
    if len(data) == hist:
        constellations.append([data[0]])
        del data[0]
        b += 1

print("Number of constellations:", len(constellations))
            