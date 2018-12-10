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
alphabet.sort()

times = []
for a in alphabet:
    times.append([a, ord(a)-4])
print(times)

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

def perform_step(steps, step):
#    step = possible(steps)[0]
    step_order.append(step)
    alphabet.remove(step)

    newSteps = []
    for a in steps:
        if step != a[0]:
            newSteps.append(a)
    return newSteps


workers = [[' ', 0], [' ', 0], [' ', 0], [' ', 0], [' ', 0]]

ticker = 0
while steps != []:
    
    # local_possible is all possible steps that no worker is working on.
    local_possible = possible(steps)
    for w in workers:
        if w[0] in local_possible:
            local_possible.remove(w[0])

    # Assign all idle workers a step to complete, if possible.
    for i in range(len(workers)):
        if workers[i][0] == ' ' and len(local_possible) > 0:
            workers[i][0] = local_possible[0]
            local_possible.remove(local_possible[0])

    # Check if a step is completed. If so, make that worker idle (for now)
    for i in range(len(workers)):
        if workers[i][0] != ' ' and workers[i][1] != 0:
            if workers[i][1] % (ord(workers[i][0])-4) == 0:
                # print(ticker, "Finished step " + str(workers[i][0]) + " in " + str(workers[i][1]) + " seconds")
                steps = perform_step(steps, workers[i][0])
                local_possible = possible(steps)
                for w in workers:
                    if w[0] in local_possible:
                        local_possible.remove(w[0])
                for j in range(len(workers)):
                    if len(local_possible) > 0 and workers[j][0] == ' ':
                        workers[j][0] = local_possible[0]
                        local_possible.remove(workers[j][0])
                    elif i == j:
                        if len(local_possible) > 0:
                            workers[j][0] = local_possible[0]
                            local_possible.remove(workers[j][0])
                        else:
                            workers[j][0] = ' '
                workers[i][1] = 0
    print(ticker, workers, local_possible, possible(steps))

    ticker += 1
    for w in range(len(workers)):
        if workers[w][0] != ' ':
            workers[w][1] += 1

ticker += ord(alphabet[0])-5

perform_step(steps, alphabet[0])

step_order_string = ""
for a in step_order:
    step_order_string += a

print(step_order_string)
print(ticker)
