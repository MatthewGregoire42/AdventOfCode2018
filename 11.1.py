serial = 9435

grid = []

for x in range(300):
    grid.append([])
    for y in range(300):
        
        rackID = x+11
        cell = rackID*(y+1)
        cell += serial
        cell *= rackID
        cell = int(str(int(cell / 100))[-1:])
        cell = cell - 5
        grid[x].append(cell)


maximum = 0
max_coord = [0, 0]
max_i = 0
for i in range(1, 301):
    for x in range(len(grid)-i):
        for y in range(len(grid[0])-i):
            total = 0
            for a in range(i):
                for b in range(i):
                    total += grid[x+a][y+b]
            if total > maximum:
                maximum = total
                max_coord = [x+1, y+1]
                max_i = i
                print("new max", max_coord, max_i, maximum)
    print("Done with", i)

print(maximum, max_coord, max_i)