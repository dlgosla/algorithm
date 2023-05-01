"""
union find 
집합을 합칠 때 parent를 통일 시켜주고
parent가 같으면 같은 집합으로 판단
"""

import sys

limit_number = 10000
sys.setrecursionlimit(limit_number)


def union(a, b):
    global parents

    a_parent = find_parent(a)
    b_parent = find_parent(b)

    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def find_parent(n):
    global parents

    if parents[n] == n:
        return n
    else:
        parents[n] = find_parent(parents[n])
        return parents[n]


def have_same_parent(a, b):
    if find_parent(a) == find_parent(b):
        return "yes"
    return "no"


n, m = map(int, input().split())

parents = [i for i in range(n + 1)]

for i in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union(a, b)
    else:
        print(have_same_parent(a, b))
