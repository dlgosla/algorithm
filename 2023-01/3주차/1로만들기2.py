"""
최소화 -> bfs
큐에 현재까지의 연산 과정을 리스트에 저장

"""

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque([[n]])  # 현재 숫자, 연산 횟수

while queue:
    lst = queue.popleft()
    node = lst[-1]

    if node == 1:  # 1이 만들어졌으면 그만
        print(len(lst) - 1)
        print(*lst)
        break

    if node % 2 == 0:  # 2로 나누어 떨어지면 2로 나눈 수를 큐에 추가
        queue.append((lst + [node // 2]))

    if node % 3 == 0:  # 3으로 나누어 떨어지면 3으로 나눈 수를 큐에 추가
        queue.append((lst + [node // 3]))

    # 1을 뺀 숫자를 큐에 추가
    queue.append(lst + ([node - 1]))
