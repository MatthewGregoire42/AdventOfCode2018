# coords = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]
coords = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input6.txt", "r") as input:
    for line in input:
        n = line[:-1].split(", ")
        n[0], n[1] = int(n[0]), int(n[1])
        coords.append(n)

right = coords[0][0]
left = coords[0][0]
top = coords[0][1]
bottom = coords[0][1]

for a in coords:
    if a[0] < left:
        left = a[0]
    if a[0] > right:
        right = a[0]
    if a[1] < top:
        top = a[1]
    if a[1] > bottom:
        bottom = a[1]

grid = []
for x in range(left, right+2):
    grid.append([])
    for y in range(top, bottom+1):
        grid[x-left].append(-1)

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for x in range(0, len(grid)):
    for y in range(0, len(grid[0])):
        mindistance = 10000
        minpoint = 0
        for a in range(0, len(coords)):
            d = distance(x+left, y+top, coords[a][0], coords[a][1])
            # print("["+str(x)+", "+str(y)+"]", coords[a], d)
            if d < mindistance:
                mindistance = d
                minpoint = a
        num_collisions = 0
        for a in coords:
            if distance(x+left, y+top, a[0], a[1]) == mindistance:
                num_collisions += 1
        if num_collisions > 1:
            minpoint = -1
        grid[x][y] = minpoint

print(grid)

to_delete = set()
for a in grid[0]:
    to_delete.add(a)
for a in grid:
    to_delete.add(a[0])
    to_delete.add(a[-1])
for a in grid[-1]:
    to_delete.add(a)
to_delete.remove(-1)

print(to_delete) # Want to be: 0, 1, 2, 5 for the test input


totals = [0]*len(coords)
for i in grid:
    for point in i:
        if point != -1:
            totals[point] += 1

newTotals = []
for i in range(0, len(totals)):
    if i not in to_delete:
        newTotals.append(totals[i])

print(max(newTotals))

        