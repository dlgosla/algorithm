"""
4
1 3
2 5
3 5
6 7

1 - 2 - 3 - 4 - 5  6 - 7 

정렬 후에 합칠 수 있을 만큼 합치고
못합치게 될 때 합쳐진 구간의 길이를 더하고
다시 그 부분부터 합칠 수 있을 만큼 합치고 반복

s = 6 e = 8
left = 5
right = 8
"""

n = int(input())

lines = []
for i in range(n):
    start, end = map(int, input().split())
    lines.append((start, end))

lines.sort()

left = lines[0][0]
right = lines[0][1]

count = 0
for i in range(1, n):
    s, e = lines[i]
    if s <= right:
        right = max(e, right)
    else:
        count += right - left
        left = s
        right = e

print(count + right - left)
