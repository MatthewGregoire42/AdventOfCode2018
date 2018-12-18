import math

ground = []
data = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input17.txt", "r") as input:
    for line in input:
        data.append(line[:-1])

# Xveins are horizontal, Yveins are vertical

veins = []

for a in data:
    startX = a.find("x=")+2
    startY = a.find("y=")+2
    if startX == 2:
        endX = a.find(",")
        endY = a.find("..")+2

        x = int(a[startX:endX])
        y = range(int(a[startY:endY-2]), int(a[endY:])+1)

        for p in y:
            veins.append([x, p])
    elif startY == 2:
        endX = a.find("..")+2
        endY = a.find(",")

        x = range(int(a[startX:endX-2]), int(a[endX:])+1)
        y = int(a[startY:endY])

        for p in x:
            veins.append([p, y])

minX = 10000
minY = 10000
maxX = 0
maxY = 0

for a in veins:
    if a[0] < minX:
        minX = a[0]
    elif a[0] > maxX:
        maxX = a[0]
    if a[1] < minY:
        minY = a[1]
    elif a[1] > maxY:
        maxY = a[1]

ground = [["."]*(maxX+1-minX+6) for i in range(maxY+1)]

# With this input, X coordinates are offset by 108 in the ground array.

for a in veins:
    ground[a[1]][a[0]-minX+3] = "#"

ground[0][500-minX+3] = "+"   # This is the spring of water

# This should be called with an x that is already offset.
def iterate(ground, x, y):
    if y > maxY or x > maxX-minX or x < 0:
        return 9999, 9999
    else:
        if ground[y+1][x] == ".":
            ground[y][x] = "|"
            return x, y+1
        elif ground[y+1][x] == "|":
            ground[y][x] = "|"
            return 9999, 9999
        elif ground[y+1][x] == "#" or ground[y+1][x] == "~":

            ground[y][x] = "|"

            overflowR = False
            overflowL = False

            tempX = x
            record = tempX
            while ground[y][tempX] != "#":
                ground[y][tempX] = "~"
                if ground[y+1][tempX] == "." or ground[y+1][tempX] == "|":
                    overflowR = True
                    record = tempX
                    break
                tempX += 1
                if tempX >= len(ground[y]):
                    overflowR = True
                    record = tempX
                    break

            tempX = x
            while ground[y][tempX] != "#":
                ground[y][tempX] = "~"
                tempX -= 1
                if ground[y+1][tempX] == "." or ground[y+1][tempX] == "|":
                    overflowL = True
                    break
                if tempX >= len(ground[y]):
                    overflowL = True
                    break
            
            solid = True

            if overflowL and overflowR:
                solid = solidGround(ground, y, tempX, record)

            if overflowL and overflowR and not solid:
                for i in range(tempX, record+1):
                    if ground[y-1][i] != "|":
                        ground[y][i] = "."
                    else:
                        ground[y][i] = "|"
                ground[y][x] = "|"
                return 9999, 9999
            elif overflowL and overflowR:
                ground[y][tempX] = "|"
                ground[y][record] = "|"
                sourceQueue.append([tempX, y+1])
                return record, y+1
            elif overflowL:
                ground[y][tempX] = "|"
                return tempX, y+1
            elif overflowR:
                ground[y][record] = "|"
                return record, y+1

            return x, y-1
        
def solidGround(ground, y, x1, x2):
    check = ground[y+1][x1+1:x2]
    if check[0] == "#" and check[-1] == "#":
        return True
    return False

sourceQueue = []

count = 0
x, y = 500-minX, 1
while True:
    try:
        if not (x == 9999 and y == 9999):
            x, y = iterate(ground, x, y)
        else:
            if len(sourceQueue) > 0:
                n = sourceQueue.pop(0)
                x, y = iterate(ground, n[0], n[1])
            else:
                break
    except IndexError:
        x, y = 9999, 9999
    count += 1
    # print(countPipes(ground))

for a in range(len(ground)):  
    while True:
        s = "".join(ground[a])
        if ".|~" in s:
            index = s.find(".|~")+2
            print(index)
            while True:
                if ground[a][index] == "~":
                    ground[a][index] = "|"
                    index += 1
                else:
                    break
        else:
            break
        
    
    while True:
        s = "".join(ground[a])
        if "~|." in s:
            index = s.find("~|.")
            while True:
                if ground[a][index] == "~":
                    ground[a][index] = "|"
                    index -= 1
                else:
                    break
        else:
            break

# Debugging statements for printing any region of the map:

# for i in range(900):
#     Xoffset = 0
#     offset = 0
#     print(str(i+offset) + " " + "".join(ground[i+offset][Xoffset:]))
# print("done", count)

def countWater(ground):
    count = 0
    for a in ground:
        for b in a:
            if b == "~":
                count += 1
    return count

print(countWater(ground))

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\output17.txt", "w") as input:
    for line in ground:
        input.write("".join(line))