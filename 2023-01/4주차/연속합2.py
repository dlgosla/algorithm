"""

dp[0][i] : 아무것도 제거하지 않았을 경우에 0부터 i번째 까지 데이터 중에서 가장 큰 연속합
dp[1][i] : 하나를 제거했을 때 0부터 i번째 까지 데이터 중에서 가장 큰 연속합

10 -4 3 1 5 6 -35 12 21 -1

"""

n = int(input())
dp = [[0] * n for i in range(2)]

arr = [int(elem) for elem in input().split()]
dp[0][0] = arr[0]

ans = dp[0][0]
for i in range(1, n):
    # 아무것도 제거하지 않았을 경우
    # 직전까지의 최대연속합에서 현재 원소를 더한 값과 현재 원소 중에서 더 큰 값 선택
    dp[0][i] = max(arr[i], dp[0][i - 1] + arr[i])

    # 제거할 경우
    # dp[1][i - 1] + arr[i] -> 이전에 이미 하나를 뺀 경우 => 하나 뺀거의 최댓값에 현재값 포함
    # dp[0][i - 1] -> 현재값을 제거할 경우 == i-1번째까지만 모두 포함할 경우
    dp[1][i] = max(dp[1][i - 1] + arr[i], dp[0][i - 1])

    ans = max(ans, dp[0][i], dp[1][i])

print(ans)
