lines = []
zero = 0
import time

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input12.txt", "r") as input:
    for line in input:
        lines.append(line[:-1])

initial = lines[0][15:]
rule = [[b for b in a.split(" => ")] for a in lines[1:]][1:]

state = list(initial)

def total(state, zero):
    output = 0
    for i in range(len(state)):
        if state[i] == "#":
            output += i+zero
    return output

# This iterate function needs to dynamically scale the size of the state area.
def trim(state, zero):
    while True:
        if state[0] == "#":
            break
        else:
            del state[0]
            zero += 1
    while True:
        if state[-1] == "#":
            break
        else:
            del state[-1]
    return zero-4

def iterate(state, rule, zero):
    operating = ["."]*4 + state + ["."]*4
    # print("".join(operating))
    output = operating.copy()
    for i in range(0, len(operating)-4):
        snip = "".join(operating[i:i+5])
        for a in rule:
            if snip == a[0]:
                output[i+2] = a[1]
    # print("".join(output))
    zero = trim(output, zero)
    # print(zero)
    return output, zero

def steady(state):
    old = state.copy()
    test = old.copy()
    test = iterate(test, rule, zero)[0]
    if test == old:
        return True
    return False

start = time.time()
gens = 0
for i in range(0, 50000000000):
    # print(total(state, zero))
    # print(total(state, zero+1))
    state, zero = iterate(state, rule, zero)
    # print("".join(state))
    if steady(state):
        gens = i
        break

print(total(state, zero+(50000000000-gens-1)))