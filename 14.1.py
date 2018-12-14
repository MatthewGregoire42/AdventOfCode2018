num_recipies = 360781

puzzle = [3, 7]

# Puzzle is the scoreboard, and a and b are the 
# indices that each elf is currently at.
def iterate(puzzle, a, b):
    elf1 = puzzle[a]
    elf2 = puzzle[b]
    total = elf1 + elf2
    if total < 10:
        puzzle.append(total)
    else:
        puzzle.append(1)
        puzzle.append(total-10)
    new_a = (a + (elf1 + 1)) % len(puzzle)
    new_b = (b + (elf2 + 1)) % len(puzzle)
    return new_a, new_b

a = 0
b = 1

count = 0
while len(puzzle) < num_recipies+20:
    a, b = iterate(puzzle, a, b)
    count += 1
    print(count)
output = puzzle[360781:]
print(output)