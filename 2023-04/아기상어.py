from collections import deque

lst = []

n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]


def solution(x, y):
    size = 2  # 물고기 사이즈
    time = 0  # 시간
    eat_count = 0  # 현재 사이즈에서 먹은 물고기 수

    q = deque([(x, y)])  # 방문해야할 좌표들
    visited = set([(x, y)])  # 방문한 노드들
    flag = False  # 그 좌표에서 먹었는 지 안먹었는 지 먹었으면 true
    answer = 0  # 총 걸린 시간

    while q:  # 큐에 원소가 있을 때

        q = deque(sorted(q))  # 위, 왼쪽 먼저 조건을 위해 소팅
        # print("q: ", q)

        for _ in range(len(q)):
            x, y = q.popleft()

            # 지금 좌표에 상어보다 크기가 작은 물고기가 있으면 먹음
            if lst[x][y] != 0 and lst[x][y] < size:
                lst[x][y] = 0
                eat_count += 1

                # 현재 기준으로 처음부터 다시 탐색해야 되니까 초기화
                q, visited = deque(), set([(x, y)])
                flag = True

                answer = time

                # 물고기를 현재 사이즈 크기만큼 먹었으면 사이즈를 키움
                if size == eat_count:
                    size += 1
                    eat_count = 0

            # 어디로 갈 지 정함
            for dx, dy in zip(dxs, dys):  # 상하좌우로 움직임
                x2, y2 = x + dx, y + dy

                # 다음으로 이동할 좌표가 범위 내에 있고, 상어보다 작으며 방문하지 않은 노드일 때 이동
                if (
                    0 <= x2 < n
                    and 0 <= y2 < n
                    and lst[x2][y2] <= size
                    and (x2, y2) not in visited
                ):
                    # print("x1,y1: ",x,y, "// x2, y2", x2, y2, " //answer: " ,answer)
                    q.append((x2, y2))
                    visited.add((x2, y2))

            if flag:
                flag = False
                break

        time += 1

    return answer


# 초기에 상어가 있는 위치를 찾음
for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            x1 = i
            y1 = j
            lst[i][j] = 0
            break

print(solution(x1, y1))
