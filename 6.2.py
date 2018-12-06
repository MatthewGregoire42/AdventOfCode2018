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
        grid[x-left].append(0)

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for x in range(0, len(grid)):
    for y in range(0, len(grid[0])):
        total_distance = 0
        for a in range(0, len(coords)):
            total_distance += distance(x+left, y+top, coords[a][0], coords[a][1])  
        if total_distance < 10000:
            grid[x][y] = 1

count = 0
for x in range(0, len(grid)):
    for y in range(0, len(grid[0])):
        if grid[x][y] == 1:
            count += 1
print(count)