data = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input23.txt", "r") as input:
    for line in input:
        l = line[:-1].split(",")
        l[0] = int(l[0][5:])
        l[1] = int(l[1])
        l[2] = int(l[2][:-1])
        l[3] = int(l[3][3:])
        data.append(l)

strongest = []
s = 0

for bot in data:
    if bot[3] > s:
        strongest = bot
        s = bot[3]


inRange = []

count = 0
for bot in data:
    distance = abs(strongest[0] - bot[0]) + abs(strongest[1]-bot[1]) + abs(strongest[2]-bot[2])
    if distance <= strongest[3]:
        count += 1
print(count)