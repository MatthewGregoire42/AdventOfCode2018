forest = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input18.txt", "r") as input:
    for line in input:
        forest.append(list(line[:-1]))

history = [[a.copy() for a in forest]]

final = 0

# Range is 10 for part 1, 1000000000 for part 2
for i in range(1000000000):
    ref = [a.copy() for a in forest]

    for j in range(len(ref)):
        for k in range(len(ref[0])):
            openSquares = 0
            trees = 0
            lumberyard = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if not (a == 0 and b == 0):
                        if j+a in range(len(ref)) and k+b in range(len(ref[0])):
                            if ref[j+a][k+b] == ".":
                                openSquares += 1
                            elif ref[j+a][k+b] == "|":
                                trees += 1
                            elif ref[j+a][k+b] == "#":
                                lumberyard += 1
            square = ref[j][k]
            if square == "." and trees >= 3:
                forest[j][k] = "|"
            elif square == "|" and lumberyard >= 3:
                forest[j][k] = "#"
            elif square == "#" and not (lumberyard >= 1 and trees >= 1):
                forest[j][k] = "."
    if forest in history:
        final = i+1
        break
    else:
        history.append([a.copy() for a in forest])
    print(i)
    
cycle = len(history) - history.index(forest)
history = history[-cycle:]

gen = (1000000000 - final) % len(history)
forest = history[gen]

w = 0
l = 0

for i in range(len(forest)):
    for j in range(len(forest[0])):
        if forest[i][j] == "|":
            w += 1
        elif forest[i][j] == "#":
            l += 1
print(l*w)                   