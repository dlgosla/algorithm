from collections import defaultdict

n = int(input())

max_end_time = 0

dp = defaultdict(int)
meetings = defaultdict(list)
for i in range(n):
    start, end = map(int, input().split())
    meetings[start].append(end)
    if end > max_end_time:
        max_end_time = end


for start_time in range(max_end_time, -1, -1):
    if meetings[start_time]:
        count = 0
        for end_time in meetings[start_time]:
            if start_time == end_time:
                count += 1
            else:
                dp[start_time] = max(
                    1 + dp[end_time], dp[start_time + 1], dp[start_time]
                )
        dp[start_time] += count
    else:
        dp[start_time] = dp[start_time + 1]

    dp[start_time - 1] = dp[start_time]

print(dp[0])
print(dp)
