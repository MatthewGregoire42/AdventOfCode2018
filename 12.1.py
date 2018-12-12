lines = []
gens = 50000000000
offset = gens*2

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input12.txt", "r") as input:
    for line in input:
        lines.append(line[:-1])

initial = lines[0][15:]
rule = [[b for b in a.split(" => ")] for a in lines[1:]][1:]

print(rule)

print(initial)

# The state array is offset by 20, so that pot 0 is at index 20
# This offset by 20 is because in this CA, the speed of light is 2
state = ["."]*(len(initial)+(offset*2)+5)

for i in range(len(state)):
    if i >= offset and i < len(initial)+offset:
        state[i] = initial[i-offset]

print("".join(state))

def iterate(state, rule):
    output = ['.', '.']
    for i in range(len(state)-2):
        if i < len(state)-5:
            snip = "".join(state[i:i+5])
        else:
            snip = "....."
        for a in rule:
            if snip == a[0]:
                output.append(a[1])
                break
    return output

def total(state):
    output = 0
    for i in range(len(state)):
        if state[i] == "#":
            output += i-offset
    return output

print(total(state))

for i in range(gens):
    state = iterate(state, rule)
    print(i, "".join(state), len(state))
print(total(state))