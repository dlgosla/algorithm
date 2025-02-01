import sys
from collections import deque

# 입력 함수를 더 간결하게 사용하기 위해 input 함수 재정의
input = sys.stdin.readline

# 12x6 크기의 필드 정보를 입력받음
data = [list(input().rstrip()) for _ in range(12)]

# 상하좌우 이동을 위한 방향(dx, dy) 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 뿌요를 아래로 당기는 함수
def down():
    for i in range(6):  # 열(column)을 기준으로 순회
        for j in range(10, -1, -1):  # 아래서부터 위로 순회
            for k in range(11, j, -1):
                # 현재 위치에 뿌요가 있고, 아래쪽이 빈 공간인 경우
                if data[j][i] != "." and data[k][i] == ".":
                    data[k][i] = data[j][i]  # 뿌요를 아래로 당김
                    data[j][i] = "."
                    break

# 4칸 이상인 뿌요를 확인하는 함수
def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 인덱스 범위를 벗어나지 않고, 같은 색상의 뿌요이며, 방문한 적이 없는 경우
            if 0 <= nx < 12 and 0 <= ny < 6 and data[nx][ny] == data[x][y] and visited[nx][ny] == 0:
                q.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = 1

# 4칸 이상인 뿌요를 지우는 함수
def delete(temp):
    for a, b in temp:
        data[a][b] = "."

ans = 0  # 연쇄 횟수를 저장하는 변수

while 1:
    flag = 0  # 연쇄가 발생했는지를 나타내는 플래그 변수
    visited = [[0] * 6 for _ in range(12)]  # 방문 체크를 위한 2차원 리스트 초기화

    for i in range(12):
        for j in range(6):
            if data[i][j] != "." and visited[i][j] == 0:  # 뿌요가 있고 방문한 적이 없는 경우
                visited[i][j] = 1  # 방문 체크
                temp = []
                bfs(i, j)  # 연결된 뿌요 확인

                if len(temp) >= 4:  # 연결된 뿌요가 4개 이상인 경우
                    flag = 1  # 연쇄가 발생했음을 표시
                    delete(temp)  # 뿌요를 지움

    if flag == 0:  # 더 이상 연쇄가 발생하지 않은 경우
        break

    down()  # 뿌요를 아래로 당김
    ans += 1  # 연쇄 횟수 증가

print(ans)  # 결과 출력