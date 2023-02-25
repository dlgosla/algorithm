n = int(input())

# metrix = [[int(x) for x in input().split()] for i in range(n)]
first_row = list(map(int, input().split()))

max_dp = [[0] * 3 for _ in range(n)]
min_dp = [[0] * 3 for _ in range(n)]
max_dp[0] = first_row
min_dp[0] = first_row

for i in range(1, n):
    for j, elem in enumerate(input().split()):
        elem = int(elem)

        max_dp[i][j] = elem
        min_dp[i][j] = elem

        if j == 0:
            max_dp[i][j] += max(max_dp[i - 1][0], max_dp[i - 1][1])
            min_dp[i][j] += min(min_dp[i - 1][0], min_dp[i - 1][1])
        elif j == 1:
            max_dp[i][j] += max(max_dp[i - 1][0], max_dp[i - 1][1], max_dp[i - 1][2])
            min_dp[i][j] += min(min_dp[i - 1][0], min_dp[i - 1][1], min_dp[i - 1][2])
        else:
            max_dp[i][j] += max(max_dp[i - 1][1], max_dp[i - 1][2])
            min_dp[i][j] += min(min_dp[i - 1][1], min_dp[i - 1][2])


print(max(max_dp[-1]), min(min_dp[-1]))
