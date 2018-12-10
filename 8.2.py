# import sys
# sys.setrecursionlimit(2000)

chars = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input8.txt", "r") as input:
    for line in input:
        n = line[:-1].split(" ")
        chars.append(n)

tree = []
for a in chars[0]:
    tree.append(int(a))

# tree = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def sumMetadata(tree, test):
    numChildren = tree[0]
    numMetadata = tree[1]
    # print(tree)
    count = 0
    del tree[0:2]
    # If tree[0] != 0, go into its children and sum up their metadata
    # Then go and sum up this node's metadata
    while numChildren != 0:
        temp, test = sumMetadata(tree, test+1)
        # print("got here", tree)
        count += temp
        numChildren -= 1
    for i in range(0, numMetadata):
        count += tree[0]
        del tree[0]
    return count, test

def value(tree):
    # print(tree)
    numChildren = tree[0]
    numMetadata = tree[1]
    del tree[0:2]
    val = 0
    if numChildren == 0:
        for i in range(numMetadata):
            val += tree[0]
            del tree[0]
    else:
        # If the node does have children, get rid of all of those.
        # Then, tack on the metadata from the beginning of the tree list.
        metadata = []
        childValues = []
        for i in range(numChildren):
            temp = value(tree)
            childValues.append(temp)
        for i in range(numMetadata):
            metadata.append(tree[0])
            del tree[0]
        for a in metadata:
            if a >= 1 and a <= numChildren:
                val += childValues[a-1]
    return val

print(value(tree))