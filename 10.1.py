# This challenge finally got me to figure out how to
# install matplotlib! I'm so happy.

# What I'm not happy about is how clunky my input parsing is.

import numpy as np 
import matplotlib.pyplot as plt

coordinates = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input10.txt", "r") as input:
    for line in input:
        data = line[10:-2].replace('velocity=<', '').replace(',', '').replace('>', '').split()
        coord = []
        for a in data:
            coord.append(int(a))
        coordinates.append(coord)

# print(coordinates)

def smallestRect(coordinates):
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0

    for c in coordinates:
        if c[0] < minX:
            minX = c[0]
        elif c[0] > maxX:
            maxX = c[0]
        if c[1] < minY:
            minY = c[1]
        elif c[1] > maxY:
            maxY = c[1]
    return abs(maxX-minX) * abs(maxY-minY)

def iterate(coordinates):
    for a in coordinates:
        a[0] += a[2]
        a[1] += a[3]

count = 0
previousRect = smallestRect(coordinates)
prev = []
while True:
    prev = coordinates.copy()
    count += 1
    iterate(coordinates)
    temp = previousRect
    previousRect = smallestRect(coordinates)
    print(count, previousRect)
    if temp < previousRect:
        print("Interesting")
        break

for a in prev:
    a[0] -= a[2]
    a[1] -= a[3]

x = []
y = []
for a in prev:
    x.append(a[0])
    y.append(-a[1])

plt.scatter(x, y)
plt.show()


