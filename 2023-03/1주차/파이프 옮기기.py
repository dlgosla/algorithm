# """
# 완전탐색, 백트랙킹

# """

# from collections import deque
# from enum import Enum, auto
# import sys

# input = sys.stdin.readline

# n = int(input())

# house = []
# for i in range(n):
#     house.append([int(elem) for elem in input().split()])

# m = len(house[0])


# def toRight(r, c):
#     if c + 1 < n and not house[r][c + 1]:
#         return True
#     return False


# def toDiagonal(r, c):
#     if not toRight(r, c):
#         return False
#     if not toDown(r, c):
#         return False
#     if house[r + 1][c + 1]:
#         return False
#     return True


# def toDown(r, c):
#     if r + 1 < n and not house[r + 1][c]:
#         return True
#     return False


# class Direction(Enum):
#     RIGHT = auto()
#     DOWN = auto()
#     DIAGONAL = auto()


# count = 0
# dq = deque([(0, 1, Direction.RIGHT)])

# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]


# while dq:
#     cr, cc, direction = dq.popleft()

#     if (cr, cc) == (n - 1, m - 1):
#         count += 1
#         continue

#     if direction in [Direction.RIGHT, Direction.DIAGONAL]:
#         if toRight(cr, cc):
#             dq.append((cr, cc + 1, Direction.RIGHT))

#     if direction in [Direction.DOWN, Direction.DIAGONAL]:
#         if toDown(cr, cc):
#             dq.append((cr + 1, cc, Direction.DOWN))

#     if toDiagonal(cr, cc):
#         dq.append((cr + 1, cc + 1, Direction.DIAGONAL))

# print(count)


import sys

input = sys.stdin.readline

n = int(input())

house = []
for i in range(n):
    house.append([int(elem) for elem in input().split()])

dp_horizontal = [[0] * n for i in range(n)]
dp_vertical = [[0] * n for i in range(n)]
dp_diagonal = [[0] * n for i in range(n)]


dp_horizontal[0][1] = 1
for i in range(2, n):
    if not house[0][i]:
        dp_horizontal[0][i] = dp_horizontal[0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        if not house[i][j]:
            dp_horizontal[i][j] = dp_horizontal[i][j - 1] + dp_diagonal[i][j - 1]
            dp_vertical[i][j] = dp_vertical[i - 1][j] + dp_diagonal[i - 1][j]

            if not (house[i - 1][j] or house[i][j - 1]):
                dp_diagonal[i][j] = (
                    dp_vertical[i - 1][j - 1]
                    + dp_horizontal[i - 1][j - 1]
                    + dp_diagonal[i - 1][j - 1]
                )

print(
    dp_diagonal[n - 1][n - 1] + dp_vertical[n - 1][n - 1] + dp_horizontal[n - 1][n - 1]
)
