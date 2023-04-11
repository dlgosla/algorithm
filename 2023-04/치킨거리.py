from itertools import combinations

n, m = map(int, input().split())
board = []
chickens = []
houses = []

for i in range(n):
    row = []
    for j, elem in enumerate(input().split()):
        elem = int(elem)
        row.append(elem)
        if elem == 2:
            chickens.append((i, j))
        if elem == 1:
            houses.append((i, j))
    board.append(row)


nr = [-1, 0, 1, 0]
nc = [0, 1, 0, -1]

min_dist = float("inf")
for i in range(1, m + 1):
    combs = combinations(chickens, i)
    for comb in combs:
        # 집마다 치킨집 까지 거리 중에 젤 가까운 거리를 더해가면서 현재 치킨집 조합의 치킨거리를 구함

        curr_comb_min_dist = 0
        # 각 집에 대해
        for (house_i, house_j) in houses:
            house_min_dist = float("inf")

            # 치킨집 마다
            for (chicken_i, chicken_j) in comb:
                # 거리를 구해서
                temp_dist = abs(chicken_i - house_i) + abs(chicken_j - house_j)

                # 이 집에서 가장 가까운 치킨 집 거리를 구함
                house_min_dist = min(house_min_dist, temp_dist)

            curr_comb_min_dist += house_min_dist

        min_dist = min(min_dist, curr_comb_min_dist)

print(min_dist)
