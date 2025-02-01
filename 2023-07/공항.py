from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a >b:
        parent[a] = b
    else:
        parent[b] = a


g = int(stdin.readline())
p = int(stdin.readline())

parent = [x for x in range(g + 1)]
res = 0

for i in range(p):
    gi = int(stdin.readline())

    data = find_parent(parent, gi)
    if data == 0:
        break
    res += 1
    union_parent(parent, data, data - 1)

print(res)