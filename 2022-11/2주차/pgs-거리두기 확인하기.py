"""
45분 소요

dfs로 주위를 방문해보면서 2칸이 넘기 전에 P가 있으면 아웃

다른 사람 풀이로 배운점
이동할 수 있는 거리 계산할 때 리스트에다 따로 저장하는 방법도 있다.
그냥 경우의 수 다 나열하는 방법으로 풀수도 있다.

"""


from collections import deque, defaultdict

PLACE_LENGTH = 5


def bfs(place):
    dq = deque()
    delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    people = []

    for i in range(PLACE_LENGTH):
        for j in range(PLACE_LENGTH):
            if place[i][j] == "P":
                people.append((i, j))

    for (r, c) in people:
        dq = deque([(r, c, 0)])
        visited = defaultdict(lambda: False)
        visited[(r, c)] = True

        while dq:
            # print(dq)
            curr_r, curr_c, count = dq.pop()

            if 0 < count <= 2 and place[curr_r][curr_c] == "P":
                return 0

            if count >= 2:
                continue

            for dr, dc in delta:
                next_r = curr_r + dr
                next_c = curr_c + dc

                if 0 <= next_r < PLACE_LENGTH and 0 <= next_c < PLACE_LENGTH:
                    if not visited[(next_r, next_c)] and place[next_r][next_c] != "X":
                        dq.append((next_r, next_c, count + 1))
                        visited[(next_r, next_c)] = True

    return 1


def solution(places):
    answer = []

    m = []
    for place in places:
        m = []
        for seats in place:
            m.append(list(seats))

        answer.append(bfs(m))
        # break

    return answer
