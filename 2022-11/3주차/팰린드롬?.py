n = int(input())
numbers = input().split()
m = int(input())

questions = []
for i in range(m):
    start, end = map(int, input().split())
    questions.append((start, end))


dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]


for jump in range(1, n):
    for start in range(0, n - jump):
        end = start + jump

        mid = (start + end) / 2

        if numbers[start] == numbers[end]:
            prev_start = start + 1
            prev_end = end - 1

            if prev_start < prev_end:
                dp[start][end] = dp[prev_start][prev_end]
            else:
                dp[start][end] = 1
        else:
            dp[start][end] = 0

# print(dp)

for (start, end) in questions:
    print(dp[start - 1][end - 1])
