"""
음수, 양수, 짝수, 홀수 경우 생각하자
시간 초과 나면 범위는 주어진 범위를 활용하자

"""

from collections import defaultdict, deque

n, k = map(int, input().split())

dq = deque()

visited = defaultdict(lambda: False)

if k < n:
    print(n - k)

else:
    dq.append((n, 0))

while dq:
    curr_number, count = dq.popleft()

    if curr_number == k:
        print(count)
        break

    if curr_number < 0:
        continue

    if curr_number > k * 2:
        continue

    if not visited[curr_number + 1]:
        dq.append((curr_number + 1, count + 1))
        visited[curr_number + 1] = True

    if not visited[curr_number - 1]:
        dq.append((curr_number - 1, count + 1))
        visited[curr_number - 1] = True

    if not visited[curr_number * 2]:
        dq.append((curr_number * 2, count + 1))
        visited[curr_number * 2] = True


# 다른 사람 풀이

"""
배운점

count 셀 때 나는 bfs 중간에 계속 끌고다녔는데 그거 말고 새로 리스트를 만들어서 인덱스로 판단할 수도 있다.
if 말고 for문의 in으로도 세가지 경우를 한번에 처리할 수 있었다.

"""

from collections import deque

# 입력값 받기
n, k = map(int, input().split())
# 움직일 수 있는 최대 좌표는 100000
max_num = 100000
# 해당 위치에 도착했을 때 시간을 표시하는 리스트
visited = [0] * (max_num + 1)  # 현재는 시작하지 않았기에 0으로 모두 초기화

# bfs 함수 정의
def bfs():
    q = deque()
    # 수빈이 출발점 위치 큐에 삽입
    q.append(n)
    while q:
        x = q.popleft()
        # 수빈이 위치가 동생의 위치와 같다면 반복문 종료
        if x == k:
            print(visited[x])
            break
        # 이동할 수 있는 방향에 대하여
        for j in (x - 1, x + 1, x * 2):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= j <= max_num and not visited[j]:
                # 이동한 위치에 현재 이동한 시간 표시
                visited[j] = visited[x] + 1
                # 큐에 추가
                q.append(j)


# bfs 실행
bfs()
