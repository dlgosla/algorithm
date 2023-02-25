import sys

from collections import defaultdict

sys.setrecursionlimit(10**5)

n = int(input())
populations = {idx + 1: p for idx, p in enumerate(map(int, input().split()))}
# populations = sorted(populations.items(), key=lambda x: x[1], reverse=True)

towns = defaultdict(list)

for i in range(n - 1):
    t1, t2 = map(int, input().split())
    # t1 -= 1
    # t2 -= 1
    towns[t1].append(t2)
    # towns[t2].append(t1)
    # if t1 < t2:
    #     towns[t1].append(t2)
    # else:
    #     towns[t2].append(t1)


a = [0] * (n + 1)
b = [0] * (n + 1)


def dfs(i):
    # for town in towns[i]:
    if not towns[i]:
        a[i] = populations[i]
        b[i] = 0

    else:
        if a[i] != 0 and b[i] != 0:
            return a[i], b[i]

        prev_a, prev_b = 0, 0

        for town in towns[i]:
            if a[town] != 0 and b[town] != 0:
                prev = (a[town], b[town])
            else:
                prev = dfs(town)

            prev_a += prev[1]
            prev_b += max(prev[0], prev[1])

            print(i, town, prev[0], prev[1])

        # print(prev_a, prev_b)
        print(i, prev_a, prev_b)
        a[i] = populations[i] + prev_a
        b[i] = prev_b

    return a[i], b[i]


for i in range(1, n + 1):
    dfs(i)
# dfs(1)
print(towns)
print(populations)

print(list(zip(a, b)))
print(max(a[1], b[1]))
