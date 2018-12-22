program = []
import time

start = time.time()

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input21.txt", "r") as input:
    for line in input:
        program.append(line[:-1])

# These function definitions copied from day 16.

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

ops = {"addr": addr, "addi": addi, "mulr": mulr, "muli": muli, 
       "banr": banr, "bani": bani, "borr": borr, "bori": bori,
       "setr": setr, "seti": seti, "gtir": gtir, "gtri": gtri, 
       "gtrr": gtrr, "eqir": eqir, "eqri": eqri, "eqrr": eqrr}

ip = int(program[0][-1])
del program[0]
registers = [0]*6

registers[0] = 0

seen = []

count = 0

while True:
    line = program[registers[ip]]
    if registers[1] == 28:
        if registers[5] not in seen:
            seen.append(registers[5])
        else:
            print(seen[-1])
            break
    op = line[0:4]
    command = [int(a) for a in line[5:].split(" ")]
    registers = ops[op](registers, command)
    registers[ip] += 1
    count += 1
    if registers[ip] >= len(program):
        break
print(registers)
end = time.time()
print("Execution took " + str(end-start) + " seconds.")