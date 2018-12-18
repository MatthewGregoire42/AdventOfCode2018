before = []
commands = []
after = []

program = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input16.txt", "r") as input:
    count = 0
    for line in input:
        if count >= 0:
            if count % 4 == 0:
                if line[0:6] != "Before":
                    count = -1
                    continue
                before.append(line[:-1])
            elif count % 4 == 1:
                commands.append(line[:-1])
            elif count % 4 == 2:
                after.append(line[:-1])
            count += 1
        else:
            program.append(line[:-1])

before = [a[9:-1].split(", ") for a in before]
for a in before:
    for b in range(len(a)):
        a[b] = int(a[b])

commands = [a.split(" ") for a in commands]
for a in commands:
    for b in range(len(a)):
        a[b] = int(a[b])

after = [a[9:-1].split(", ") for a in after]
for a in after:
    for b in range(len(a)):
        a[b] = int(a[b])

program = [a.split(" ") for a in program[1:]]
for a in program:
    for b in range(len(a)):
        a[b] = int(a[b])

# All of these commands take in a register state 
# (four numbers long) and a command (3 numbers long).

def addr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] + registers[b]
    return output

def addi(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] + b
    return output

def mulr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] * registers[b]
    return output

def muli(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] * b
    return output

def banr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] & registers[b]
    return output

def bani(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] & b
    return output

def borr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] | registers[b]
    return output

def bori(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    output[c] = registers[a] | b
    return output

def setr(registers, command):
    output = registers.copy()
    a, c = command[0], command[2]
    output[c] = registers[a]
    return output

def seti(registers, command):
    output = registers.copy()
    a, c = command[0], command[2]
    output[c] = a
    return output

def gtir(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if a > registers[b]:
        output[c] = 1
    else:
        output[c] = 0
    return output

def gtri(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if registers[a] > b:
        output[c] = 1
    else:
        output[c] = 0
    return output

def gtrr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if registers[a] > registers[b]:
        output[c] = 1
    else:
        output[c] = 0
    return output

def eqir(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if a == registers[b]:
        output[c] = 1
    else:
        output[c] = 0
    return output

def eqri(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if registers[a] == b:
        output[c] = 1
    else:
        output[c] = 0
    return output

def eqrr(registers, command):
    output = registers.copy()
    a, b, c = command[0], command[1], command[2]
    if registers[a] == registers[b]:
        output[c] = 1
    else:
        output[c] = 0
    return output

opcodes = [addr, addi, mulr, muli, 
           banr, bani, borr, bori,
           setr, seti, gtir, gtri, 
           gtrr, eqir, eqri, eqrr]

possible = [(i, op) for i in range(16) for op in opcodes]

for i in range(len(before)):
    for op in opcodes:
        output = op(before[i], commands[i][1:])
        if output != after[i]:
            if (commands[i][0], op) in possible:
                possible.remove((commands[i][0], op))

definitions = {}

while len(possible) > 16:
    for i in range(16):
        count = 0
        p = ()
        for pair in possible:
            if i == pair[0]:
                count += 1
                p = pair
        if count == 1:
            definitions[p[0]] = p[1]
            for pair in possible:
                if pair[0] != i and pair[1] == definitions[i]:
                    possible.remove(pair)


# By this point, the possible array has the correct opcodes
# assigned to every function, so the example code can be run.

registers = [0, 0, 0, 0]
for line in program:
    func = possible[line[0]][1]
    registers = func(registers, line[1:])

print(registers)