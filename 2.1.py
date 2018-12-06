def count(string, char):
    count = 0
    for c in string:
        if char == c:
            count += 1
    return count

ids = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input2.txt", "r") as input:
    for line in input:
        ids.append(line[:-1])

num2s = 0
num3s = 0

for id in ids:
    num2s_local = 0
    num3s_local = 0
    for char in id:
        num = count(id, char)
        if num == 2 and num2s_local == 0:
            num2s += 1
            num2s_local += 1
        elif num == 3 and num3s_local == 0:
            num3s += 1
            num3s_local += 1

checksum = num2s*num3s
print(checksum)
        