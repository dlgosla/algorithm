n = int(input())

row = [0] * n
count = 0


def isPromising(x):
    for i in range(x):
        # 같은 열에 다른 퀸이 있는 경우, 대각선에 다른 퀸이 있는 경우
        # 전체 행을 돌면서 같은 열이 있는 지 확인
        # 같은 대각선 끼리는 행의 차이와 열의 차이가 같
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queen(x):
    global count
    if x == n:  # 모든 퀸 배치 완료
        count += 1
        return

    for i in range(n):
        row[x] = i  # x행 i열에 퀸 배치
        if isPromising(x):
            n_queen(x + 1)


n_queen(0)
print(count)
