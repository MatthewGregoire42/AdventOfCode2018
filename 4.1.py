times = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input4.txt", "r") as input:
    for line in input:
        times.append(line[:-1])

times.sort()

guards = {}

for a in times:
    if "begins shift" in a:
        guards[a[26:30]] = 0

guard = ""
count = 0
total = 0
for a in range(0, len(times)):
    if "begins shift" in times[a]:
        guard = times[a][26:30]
    if "falls asleep" in times[a]:
        guards[guard] += (int(times[a+1][15:17]) - int(times[a][15:17]))

max = 0
maxguard = ""
for a in guards:
    if guards[a] > max:
        maxguard = a
        max = guards[a]
print(max)
print(maxguard)

sleeptimes = [0]*60

for a in range(0, len(times)):
    if "begins shift" in times[a]:
        guard = times[a][26:30]
    if "falls asleep" in times[a] and guard == maxguard:
        for i in range(int(times[a][15:17]), int(times[a+1][15:17])):
            sleeptimes[i] += 1

maxi = 0
m = 0
for i in range(0, len(sleeptimes)):
    if sleeptimes[i] > m:
        m = sleeptimes[i]
        maxi = i
print(maxi)