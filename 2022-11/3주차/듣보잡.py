from collections import defaultdict


n, m = map(int, input().split())

unknowns = defaultdict(lambda: False)
for i in range(n):
    unknowns[input().strip()] = True

answer = []
count = 0
for j in range(m):
    unheared = input().strip()
    if unknowns[unheared]:
        answer.append(unheared)
        count += 1

print(count)
for unknown in sorted(answer):
    print(unknown)
