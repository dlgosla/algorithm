"""
LIS -> dp

10 20 10 30 20 50
"""

n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j] + 1, dp[i])

order = max(dp)
print(order)

"""
dp에는 앞 원소들보다 몇번째로 큰 지에 대한 순서가 저장됨
예를들어 1 3 2 라는 값을 입력한다면 dp에는 [1,2,2] 가 저장된다. 
그러면 1은 1번째, 3과 2는 2번째라는 뜻

"""
sequence = []
for i in range(n - 1, -1, -1):
    if order == dp[i]:
        sequence.append(a[i])
        order -= 1

sequence.reverse()
print(*sequence)
