n = 10


def fibo(n):
    if n < 3:
        return 1

    return fibo(n - 2) + fibo(n - 1)


dp = [0, 1, 1]
for i in range(3, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])


def fibo2(n):
    if n < 3:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b

    return b


print("재귀: ", fibo(n))
print("dp: ", dp[n])
print("반복문: ", fibo2(n))
