n, m = map(int, input().split())

matrix = []


for i in range(n):
    matrix.append(list(input()))

# 8x8에서 나올 수 있는 올바른 체스판 종류 - 제일 첫번째 색이 검정색인 체스판
black_started_chess = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

# 8x8에서 나올 수 있는 올바른 체스판 종류 - 제일 첫번째 색이 흰색인 체스판
white_started_chess = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

# 최소 색칠 횟수
min_coloring_count = 1e9

# 8x8행렬을 만들 수 있는 가짓 수 대로 만듦
for i in range(n - 7):
    for j in range(m - 7):

        # 만들어진 8x8 행렬
        temp_chess = [lst[j : j + 8] for lst in matrix[i : i + 8]]

        # 첫번째가 검정색인 체스판과 다른 부분
        black_count = 0

        # 첫번째가 흰색인 체스판과 다른 부분
        white_count = 0

        # 8x8 행렬이 체스판과 얼마나 다른 지 비교
        for k in range(8):
            for l in range(8):
                # 첫번째가 흰색인 체스판과 지금 이 행렬에 다른 부분이 있으면
                if temp_chess[k][l] != white_started_chess[k][l]:
                    # white_count 1증가
                    white_count += 1

                # 첫번째가 검정색인 체스판과 지금 이 행렬에 다른 부분이 있으면
                if temp_chess[k][l] != black_started_chess[k][l]:
                    # black_count 1증가
                    black_count += 1

        # 둘 중에서 최솟값으로 min_count 설정
        min_count = min(black_count, white_count)

        # 만들 수 있는 모든 행렬에서 최솟값이 되도록 min_coloring_count를 업데이트
        if min_count < min_coloring_count:
            min_coloring_count = min_count

print(min_coloring_count)
