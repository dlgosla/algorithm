"""
백트랙킹

"""

n, m, h = map(int, input().split())
ladders = [[False] * n for i in range(h)]
min_count = -1

for i in range(m):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = True


def check():
    # 1열부터
    for j in range(n):
        col = j
        # 행은 계속 증가, 열은 이동할 수 있으면 이동
        for i in range(h):
            if ladders[i][col]:
                col += 1
            elif col - 1 >= 0 and ladders[i][col - 1]:
                col -= 1

        if col != j:
            return False

    return True


def backtracking(count, start, max):
    global min_count

    if count == max:
        if check():
            min_count = count
        return

    for r in range(start, h):
        for c in range(n - 1):
            if not (ladders[r][c] + ladders[r][c - 1] + ladders[r][c + 1]):
                ladders[r][c] = True
                backtracking(count + 1, start, max)
                ladders[r][c] = False


for p in range(4):
    if min_count != -1:
        break
    backtracking(0, 0, p)

print(min_count)
