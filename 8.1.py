chars = []

with open("C:\\Users\\matth\\Documents\\Documents\\Advent of Code\\input8.txt", "r") as input:
    for line in input:
        n = line[:-1].split(" ")
        chars.append(n)

tree = []
for a in chars[0]:
    tree.append(int(a))

# tree = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

# class Node:
#     numChildren = 0
#     numMetadata = 0
#     children = []
#     metadata = []

#     def __init__(self, children, metadata):
#         self.childen = children
#         self.metadata = metadata

#     @classmethod
#     def makeTree(self, input):
#         root = Node([], [])
#         root.numChildren = input[0]
#         root.numMetadata = input[1]
#         input = input[2:]
#         for i in range(0, root.numChildren):
#             child, input = Node.makeTree(input)
#             root.children.append(child)
#         for i in range(root.numMetadata):
#             root.metadata.append(input[2+i])
#         return root, input
# try:
#     root = Node.makeTree(tree)[0]
# except RecursionError:
#     print("oops")

def sumMetadata(tree):
    numChildren = tree[0]
    numMetadata = tree[1]
    # print(tree)
    count = 0
    del tree[0:2]
    # If tree[0] != 0, go into its children and sum up their metadata
    # Then go and sum up this node's metadata
    while numChildren != 0:
        temp, tree = sumMetadata(tree)
        # print("got here", tree)
        count += temp
        numChildren -= 1
    for i in range(0, numMetadata):
        count += tree[0]
        del tree[0]
    return count, tree
    

print(sumMetadata(tree))