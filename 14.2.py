end_sequence = [3, 6, 0, 7, 8, 1]
# end_sequence = [5, 9, 4, 1, 4]

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

def finished(puzzle, end_sequence):
    if puzzle[len(puzzle)-len(end_sequence):] == end_sequence or puzzle[len(puzzle)-len(end_sequence)-1:-1] == end_sequence:
        return True
    else:
        return False

a = 0
b = 1
print(puzzle)
while len(puzzle) < len(end_sequence):
    a, b = iterate(puzzle, a, b)
    print(puzzle)

count = 0
while not finished(puzzle, end_sequence):
    a, b = iterate(puzzle, a, b)
    count += 1
    if count % 10000 == 0:
        print(int(count/10000))
print(len(puzzle)-len(end_sequence))
print(puzzle[len(puzzle)-len(end_sequence)-1:])