"""
25114

01
0001
1010
1020

"""

s = input()
n = len(s)

if s == "":
    print(0)
    quit()

dp = [0] * (n)
dp[0] = 0 if s[0] == "0" else 1

for i in range(1, n):
    num = int(s[i - 1] + s[i])
    if int(s[i]) != 0:
        dp[i] = dp[i - 1]

    if 10 <= num <= 26:
        if i == 1:
            dp[i] += 1
        else:
            dp[i] += dp[i - 2]


print(dp[-1] % 1000000)
