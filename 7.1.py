steps = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input7.txt", "r") as input:
    for line in input:
        n = line[:-1].split(" ")
        steps.append([n[1], n[7]])

# steps = [['C', 'A'], ['C', 'F'], ['A', 'B'], ['A', 'D'], ['B', 'E'], ['D', 'E']]

all_steps = set()
for a in steps:
    all_steps.add(a[0])
    all_steps.add(a[1])

alphabet = []
for a in all_steps:
    alphabet.append(a)

# If a step has any prequisites, it can't be completed.
def available(step):
    for i in steps:
        if step == i[1]:
            return False
    return True

def possible(steps):
    output = []
    for a in alphabet:
        if available(a):
            output.append(a)
    output.sort()
    return output

step_order = []

def perform_step(steps):
    step = possible(steps)[0]
    step_order.append(step)
    alphabet.remove(step)

    newSteps = []
    for a in steps:
        if step != a[0]:
            newSteps.append(a)
    return newSteps

while steps != []:
    steps = perform_step(steps)
    print(possible(steps))

steps = perform_step(steps)

step_order_string = ""
for a in step_order:
    step_order_string += a

print(step_order_string)