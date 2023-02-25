"""
abcde

길이가 2일 경우
ab -> a의 행 * a의 열 * b의 열
bc
cd
de 

--

길이가 3일 경우
abc -> ab(c), a(bc)중에서 최솟값
bcd 
cde

--

ab(c), a(bc)중에서 최솟값을 구하는 법

ab(c)의 최솟값 구하기
-> ab의 연산 최솟값 + ab와 c를 합치는 연산 횟수
-> ab의 연산 최솟값 + a의 행 * b의 열 * c의 열

왜?
a = 5 x 3
b = 3 x 2
c = 2 x 6

ab = 5(a의 행) x 2(b의 열)
c = 2 x 6

ab(c)의 연산 최솟값
-> ab의 연산 최솟값 + a의 행(5) * b의 열(2) * c의 열(6)

a(bc)
-> bc의 연산 최솟값 + a의 행 * a의 열 * c의 열

따라서
abc의 연산 최솟 값 = min(ab(c), a(bc))
d[a][c] = min(d[a][b] + a행*b열*c열, d[b][c] + b행*b열*c열)

---
d[i]의 의미

d[i][j] = i부터 j까지 연산 최솟값

---
점화식 세우기

abcde 연산 최솟값 
= min(
    a/bcde, -> d[a][a] + d[b][e] + a열 * a열 * e열
    ab/cde, -> d[a][b] + d[c][e] + a열 * b열 * e열
    abc/de, -> d[a][c] + d[d][e] + a열 * c열 * e열
    abcd/e  -> d[a][d] + d[e][e] + a열 * d열 * e열
)
바뀌는 부분을 k로 대치하면됨
k는 시작위치 ~ 끝위치 -1

d[i][j] = i부터 k까지 연산 최솟값 + k부터 j까지 연산 최솟값 + 앞에 두개를 연산하는 데 드는 연산 횟수
d[i][j] = d[i][k] + d[k+1][j] + i행 * k열 * j열 


"""

n = int(input())

d = [[0 for _ in range(n)] for _ in range(n)]
metrices = []

for i in range(n):
    r, c = map(int, input().split())
    metrices.append((r, c))

# abcde 일경우
# ab, bc, cd
# abc, bcd
# abcd, bcde
# abcde
for i in range(1, n):  # 시작위치 + i = 끝위치
    for j in range(0, n - i):  # 시작 위치
        start = j
        end = j + i

        # 길이가 2일 경우 (ab,bc)
        # a -> 5x3, b -> 3x2
        # ab = 5 x 3 x 2 = a행 * a열 * b열
        if i == 1:
            d[start][end] = metrices[start][0] * metrices[start][1] * metrices[end][1]

        else:
            # abcde의 연산 최솟값 = min(a/bcde,ab/cde, abc/de, abcd/e)
            # ab/cde 계산법 -> a의 행(i) x b의 열(k) x e의 열(j+i) + ab연산 최솟값(d[i][k]) + cde연산  최솟값(d[k+1][j+i])
            d[start][end] = 2**32
            for k in range(start, end):
                d[start][end] = min(
                    d[start][end],
                    d[start][k]
                    + d[k + 1][end]
                    + metrices[start][0] * metrices[k][1] * metrices[end][1],
                )


print(d[0][n - 1])
