def solution(rows, columns, queries):
    answer = []

    m = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]

    for query in queries:
        # 탐색해야할 사각형에서 왼쪽 위(시작) 좌표
        start_row = query[0] - 1
        start_col = query[1] - 1

        # 탐색해야할 사각형에서 오른쪽 아래 좌표
        end_row = query[2] - 1
        end_col = query[3] - 1

        # 오른쪽, 아래, 왼쪽, 위 순서로 탐색해야하니까
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        # 시작위치를 r,c(현재 탐색할 좌표)에 넣어줌
        r = start_row
        c = start_col

        # 어느 방향으로 진행할 지
        # 예를들어 0 이면 (dr[0], dc[0]) = (0,1) 즉 오른쪽 방향으로 하나씩 늘려가는 방향이라는 뜻
        direction = 0

        # 현재 위치에 넣어줄 숫자
        # 처음에는 시작 숫자를 넣어줘야 하니까 초기화
        curr_num = m[start_row][start_col]

        # 최솟값
        min_num = 1e9

        while True:
            # 다음 좌표
            nr = r + dr[direction]
            nc = c + dc[direction]

            # 다음 좌표가 탐색 범위를 벗어나면
            if not start_row <= nr <= end_row or not start_col <= nc <= end_col:
                # direction이 3(위로)인데 다음위치가 범위를 벗어났다면
                # 사각형 테두리 탐색을 완료해서 다시 처음으로 돌아왔다는 뜻이니까 끝냄
                if direction == 3:
                    break

                # 탐색 방향 변경
                direction += 1
                continue

            next_num = m[nr][nc]

            # 다음 위치에 현재 숫자를 넣음
            m[nr][nc] = curr_num

            # 다음 위치에 있는 숫자를 또 그 다음 위치에 넣어 줘야 하기 때문에 업데이트 해줌
            curr_num = next_num

            # 다음 위치를 현재 위치로 좌표 업데이트
            r, c = nr, nc

            # 최솟값 찾기
            if curr_num < min_num:
                min_num = curr_num

        # 최솟값을 답에 추가
        answer.append(min_num)

    return answer


print(
    solution(
        6,
        6,
        [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]],
    )
)
