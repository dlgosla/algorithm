"""


"""

s = input()
s_len = len(s)
palindrome = [[True if i == j else False for j in range(s_len)] for i in range(s_len)]

# 팰린드롬인 것 찾기
for jump in range(1, s_len):
    for i in range(s_len - jump):
        j = i + jump
        if jump == 1:
            if s[i] == s[j]:
                palindrome[i][j] = True
        else:
            if palindrome[i + 1][j - 1]:
                if s[i] == s[j]:
                    palindrome[i][j] = True

result = [float("inf")] * (s_len + 1)
result[-1] = 0
# s[1]~s[end]의 부분문자열에 존재하는 최소 팰린드롬 개수
"""
anaaba라면
an
ana
anaa
anaab
anaaba

팰린드롬일 경우
result[end] = min(result[end], result[start - 1] + 1)
아닐경우
result[end] = min(result[end], result[end - 1] + 1)

(anaaba) -> min(max, 3+1) = 4
a(naaba) -> min(4, 4) = 4
an(aaba) -> min(4, 4) = 4
ana(aba) -> min(4, 2) = 2

"""
for end in range(s_len):
    for start in range(end + 1):
        if palindrome[start][end]:
            result[end] = min(result[end], result[start - 1] + 1)
        else:
            result[end] = min(result[end], result[end - 1] + 1)

print(result[s_len - 1])
