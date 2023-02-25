"""
단조 감소 -> 그리디


"""

n = int(input())

metrix = []

for i in range(n):
    r, c = map(int, input().split())
    metrix.append((r, c))


prev_r, prev_c = metrix[-1]
count = 0
for i in range(n - 2, -1, -1):
    count += prev_r * prev_c * metrix[i][0]
    prev_r = metrix[i][0]

print(count)
