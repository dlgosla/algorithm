n = int(input())
flag = False
passage = [["X"] * n for _ in range(n)]
teachers = []

for i in range(n):
    for j, elem in enumerate(input().split()):
        if elem != "X":
            passage[i][j] = elem
        if elem == "T":
            teachers.append((i, j))


def able_to_monitor():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    for (i, j) in teachers:
        for _dr, _dc in zip(dr, dc):
            cr = i
            cc = j

            while True:
                nr = cr + _dr
                nc = cc + _dc

                if not (0 <= nr < n and 0 <= nc < n):
                    break

                if passage[nr][nc] == "O":
                    break

                if passage[nr][nc] == "S":
                    return True

                cr = nr
                cc = nc

    return False


def backtracking(count):
    global flag
    if count == 3:
        if not able_to_monitor():
            flag = True
            return

    else:
        for i in range(n):
            for j in range(n):
                elem = passage[i][j]
                if elem == "X":
                    passage[i][j] = "O"
                    backtracking(count + 1)
                    passage[i][j] = "X"


backtracking(0)
if flag:
    print("YES")
else:
    print("NO")
