times = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input4.txt", "r") as input:
    for line in input:
        times.append(line[:-1])

times.sort()

guards = []

for a in times:
    if "begins shift" in a:
        guards.append(a[26:30])

for a in range(0, len(times)):
    if "begins shift" in times[a]:
        guards.append(times[a][26:30])

sleepmax = 0
sleepmaxtime = 0
maxguard = ""
currentguard = ""
for guard in guards:
    # Construct the sleeptimes array
    sleeptimes = [0]*60
    for a in range(0, len(times)):
        if "begins shift" in times[a]:
            currentguard = times[a][26:30]
        if "falls asleep" in times[a] and currentguard == guard:
            for i in range(int(times[a][15:17]), int(times[a+1][15:17])):
                sleeptimes[i] += 1
    print(sleeptimes)
    
    # Determine if this guard sleeps the most at a certain minute
    maxi = 0
    m = 0
    for i in range(0, len(sleeptimes)):
        if sleeptimes[i] > m:
            m = sleeptimes[i]
            maxi = i
    if m > sleepmax:
        sleepmax = m
        print(m)
        sleepmaxtime = maxi
        maxguard = guard

print(maxguard, sleepmaxtime, sleepmax)