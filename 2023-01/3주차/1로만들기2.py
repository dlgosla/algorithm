"""
1로 만들기

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.


"""

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque([[n]])  # 현재 숫자, 연산 횟수

min_count = 10000000

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
