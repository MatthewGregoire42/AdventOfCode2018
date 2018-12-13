data = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input13.txt", "r") as input:
    for line in input:
        data.append(line[:-1])

graph = []
for i in range(len(data)):
    graph.append([])
    for char in data[i]:
        graph[i].append(char)

## NOTE: this assumes that the lower-right character of the graph is blank. This line
## must be adjusted if the graph has a turn there.
graph[-1].append(" ")

# This array symbolizes an array of carts.
# Each cart is represented by its current location, direction, and its next turn decision.
# The last element is used in each tick, to make sure that the cart hasn't yet moved.
carts = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == ">":
            carts.append([[i, j], "right", "left"])
        elif graph[i][j] == "<":
            carts.append([[i, j], "left", "left"])
        elif graph[i][j] == "v":
            carts.append([[i, j], "down", "left"])
        elif graph[i][j] == "^":
            carts.append([[i, j], "up", "left"])

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == ">" or graph[i][j] == "<":
            graph[i][j] = "-"
        elif graph[i][j] == "v" or graph[i][j] == "^":
            graph[i][j] = "|"

# define iterate on graph and carts
def iterate(graph, carts):

    # we want to first sort by x coordinate (cart[0][1]) then by y (cart[0][0])
    for i in range(len(carts)-1):
        cart = carts[i]
        nextCart = carts[i+1]
        if nextCart[0][1] < cart[0][1]:
            temp = cart
            carts[i] = nextCart
            carts[i+1] = temp
        elif nextCart[0][1] == cart[0][1] and nextCart[0][0] < cart[0][0]:
            temp = cart
            carts[i] = nextCart
            carts[i+1] = temp
    
    output = carts.copy()

    for c in carts:
        x = c[0][0]
        y = c[0][1]
        direction = c[1]
        tile = graph[x][y]
        if tile == "|":
            if direction == "up":
                c[0][0] -= 1
            elif direction == "down":
                c[0][0] += 1
        elif tile == "-":
            if direction == "right":
                c[0][1] += 1
            elif direction == "left":
                c[0][1] -= 1
        elif tile == "/":
            if direction == "up":
                c[1] = "right"
                c[0][1] += 1
            elif direction == "down":
                c[1] = "left"
                c[0][1] -= 1
            elif direction == "left":
                c[1] = "down"
                c[0][0] += 1
            elif direction == "right":
                c[1] = "up"
                c[0][0] -= 1
        elif tile == "\\":
            if direction == "up":
                c[1] = "left"
                c[0][1] -= 1
            elif direction == "down":
                c[1] = "right"
                c[0][1] += 1
            elif direction == "left":
                c[1] = "up"
                c[0][0] -= 1
            elif direction == "right":
                c[1] = "down"
                c[0][0] += 1
        elif tile == "+":
            switch = c[2]
            if direction == "up":
                if switch == "left":
                    c[2] = "straight"
                    c[1] = "left"
                    c[0][1] -= 1
                elif switch == "straight":
                    c[2] = "right"
                    c[0][0] -= 1
                elif switch == "right":
                    c[2] = "left"
                    c[1] = "right"
                    c[0][1] += 1
            elif direction == "down":
                if switch == "left":
                    c[2] = "straight"
                    c[1] = "right"
                    c[0][1] += 1
                elif switch == "straight":
                    c[2] = "right"
                    c[0][0] += 1
                elif switch == "right":
                    c[2] = "left"
                    c[1] = "left"
                    c[0][1] -= 1
            elif direction == "left":
                if switch == "left":
                    c[2] = "straight"
                    c[1] = "down"
                    c[0][0] += 1
                elif switch == "straight":
                    c[2] = "right"
                    c[0][1] -= 1
                elif switch == "right":
                    c[2] = "left"
                    c[1] = "up"
                    c[0][0] -= 1
            elif direction == "right":
                if switch == "left":
                    c[2] = "straight"
                    c[1] = "up"
                    c[0][0] -= 1
                elif switch == "straight":
                    c[2] = "right"
                    c[0][1] += 1
                elif switch == "right":
                    c[2] = "left"
                    c[1] = "down"
                    c[0][0] += 1
        # Collision detection
        for c in range(len(carts)):
            for d in range(len(carts)):
                if carts[c][0] == carts[d][0] and carts[c] != carts[d]:
                    # print("collision! at", str(carts[c][0][1]) + "," + str(carts[c][0][0]))
                    if carts[c] in output:
                        output.remove(carts[c])
                    if carts[d] in output:
                        output.remove(carts[d])
    return output                

def represent(graph, carts):
    output = [a.copy() for a in graph]
    for c in carts:
        if c[1] == "up":
            output[c[0][0]][c[0][1]] = "^"
        elif c[1] == "down":
            output[c[0][0]][c[0][1]] = "v"
        elif c[1] == "left":
            output[c[0][0]][c[0][1]] = "<"
        elif c[1] == "right":
            output[c[0][0]][c[0][1]] = ">"
    for a in output:
        print("".join(a))
represent(graph,carts)
count = 0
while len(carts) > 1:
    carts = iterate(graph, carts)
    count += 1
    print(count)
    # represent(graph, carts)

print("Final cart at", carts[0][0][1], carts[0][0][0])
