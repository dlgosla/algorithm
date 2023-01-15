n = int(input())

min_dp = [[0] * 3 for _ in range(n)]

for i in range(0, n):
    for j, elem in enumerate(input().split()):
        elem = int(elem)
        min_dp[i][j] = elem

        if i == 0:
            continue

        if j == 0:
            min_dp[i][j] += min(min_dp[i - 1][1], min_dp[i - 1][2])
        elif j == 1:
            min_dp[i][j] += min(min_dp[i - 1][0], min_dp[i - 1][2])
        else:
            min_dp[i][j] += min(min_dp[i - 1][0], min_dp[i - 1][1])

print(min(min_dp[-1]))
