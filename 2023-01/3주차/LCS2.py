"""
숫자 대신 문자열 자체를 저장
[['', '', '', '', '', '', ''], 
['', '', 'A', 'A', 'A', 'A', 'A'], 
['', 'C', 'C', 'C', 'AC', 'AC', 'AC'], 
['', 'C', 'CA', 'CA', 'CA', 'ACA', 'ACA'], 
['', 'C', 'CA', 'CA', 'CA', 'ACA', 'ACA'], 
['', 'C', 'CA', 'CA', 'CA', 'ACA', 'ACAK'], 
['', 'C', 'CA', 'CAP', 'CAP', 'CAP', 'ACAK']]

"""

s1 = input()
s2 = input()

dp = [["" for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        c1 = s1[i - 1]
        c2 = s2[j - 1]

        if c1 == c2:
            dp[i][j] = dp[i - 1][j - 1] + c1
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

# print(dp)
print(len(dp[-1][-1]))
print(dp[-1][-1])
