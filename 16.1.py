before = []
commands = []
after = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input16.txt", "r") as input:
    count = 0
    for line in input:
        if count % 4 == 0:
            if line[0:6] != "Before":
                break
            before.append(line[:-1])
        elif count % 4 == 1:
            commands.append(line[:-1])
        elif count % 4 == 2:
            after.append(line[:-1])
        count += 1

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

threeOrMore = 0

for i in range(len(before)):
    correct = 0
    for op in opcodes:
        output = op(before[i], commands[i][1:])
        print(i, before[i])
        if output == after[i]:
            correct += 1
    if correct >= 3:
        threeOrMore += 1
    print(i, correct)

print("")
print(threeOrMore)