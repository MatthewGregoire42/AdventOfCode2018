# Actual: numPlayers = 411, last_marble = 72059

import time
start = time.time()

numPlayers = 411
last_marble = 7205900

players = [0]*numPlayers

marbles = [0, 1]
current_marble = [1]

def add_marble(n):
    if n % 23 != 0:
        newPosition = (current_marble[0] + 2) % len(marbles)
        marbles.insert(newPosition, n)
        current_marble[0] = newPosition
    else:
        current_marble[0] = (current_marble[0] - 7) % len(marbles)
        score = n + marbles[current_marble[0]]
        players[n % numPlayers] += score
        marbles.pop(current_marble[0])


for i in range(2, last_marble+1):
    add_marble(i)
    # print(marbles, marbles[current_marble[0]])
    if i % 10000 == 0:
        print(i)

print(max(players))

end = time.time()
print("Execution took " + str(end-start) + " seconds.")