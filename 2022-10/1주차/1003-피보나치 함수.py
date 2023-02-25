dp = [-1] * 41
zero_count = [0] * 41
one_count = [0] * 41

dp[0] = 0
dp[1] = 1

zero_count[0] = 1
one_count[1] = 1


def fibo(n):
    if dp[n] != -1:
        return

    for i in range(2, n + 1):
        # dp[i] = dp[i - 2] + dp[i - 1]
        zero_count[i] = zero_count[i - 2] + zero_count[i - 1]
        one_count[i] = one_count[i - 2] + one_count[i - 1]


t = int(input())

for i in range(t):
    n = int(input())

    fibo(n)

    print(zero_count)
    print(one_count)

    print(dp)

    # print(zero_count[n], one_count[n])

    if n == 0:
        print(0, 1)

    else:
        print(dp[n - 1], dp[n])
