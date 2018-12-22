depth = 11109
target = [9, 731]

cave = []
for i in range(target[1]+1):
    cave.append([])
    for j in range(target[0]+1):
        cave[i].append(False)

def erosion(x, y):
    return (geo_index(x, y) + depth) % 20183

def geo_index(x, y):
    if y == 0:
        ans = x*16807
        cave[y][x] = ans
        return ans
    elif x == 0:
        ans = y*48271
        cave[y][x] = ans
        return ans
    elif x == target[0] and y == target[1]:
        return 0
    else:
        if cave[y][x] != False:
            return cave[y][x]
        else:
            ans = erosion(x-1, y) * erosion(x, y-1)
            cave[y][x] = ans
            return ans


def region_type(x, y):
    return erosion(x, y) % 3

risk = 0
for i in range(target[0]+1):
    for j in range(target[1]+1):
        risk += region_type(i, j)

print(risk)