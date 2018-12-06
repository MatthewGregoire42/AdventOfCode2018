claims = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input3.txt", "r") as input:
    for line in input:
        newline = line[:-1].split()

        newline[0] = newline[0][1:]
        newline.remove("@")
        newline[1] = newline[1][:-1]
        newline[1] = newline[1].split(",")
        newline[2] = newline[2].split("x")

        claims.append(newline)

for x in claims:
    x[0] = int(x[0])
    for i in range(1, 3):
        for j in range(0, 2):
            x[i][j] = int(x[i][j])

# Within claims, each sub-array is a separate claim.
# The first index is the claim number, the second is
# the claim x and y offset, and the third is the
# claim width and height.

fabric = []

for i in range(0, 1000):
    fabric.append([])
    for j in range(0, 1000):
        fabric[i].append(0)

for claim in claims:
    startX = claim[1][0]
    startY = claim[1][1]
    width = claim[2][0]
    height = claim[2][1]
    for i in range(0, width):
        for j in range(0, height):
            interest = fabric[startX + i][startY + j]
            if interest == 0:
                fabric[startX + i][startY + j] = 1
            elif interest == 1:
                fabric[startX + i][startY + j] = 2

for claim in claims:
    startX = claim[1][0]
    startY = claim[1][1]
    width = claim[2][0]
    height = claim[2][1]
    numOverlap = 0
    for i in range(0, width):
        for j in range(0, height):
            interest = fabric[startX + i][startY + j]
            if interest == 2:
                numOverlap = 1
    if numOverlap == 0:
        print(claim[0])
        break

count = 0
for x in fabric:
    for y in x:
        if y == 2:
            count += 1

# count is the number of square inches that overlap