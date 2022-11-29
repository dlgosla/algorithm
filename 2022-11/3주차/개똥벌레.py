"""


"""

from collections import defaultdict
import bisect
import sys

input = sys.stdin.readline

n, h = map(int, input().split())

dict = defaultdict(int)

top = []  # 종유석
bottom = []  # 석순
for i in range(n):
    number = int(input())
    if i % 2 == 0:
        bottom.append(number)
    else:
        top.append(number)

bottom.sort()
top.sort()

min_broken_count = n
range_count = 0
for i in range(1, h + 1):
    # 포함안되는 거 찾기
    # i 보다 더 작은 값 중에서 최댓값 인덱스
    # 1,3,5 -> i == 2(2번째 구간에서) -> 1 -> 1개만 안부수고 통과가능 2개는 부수고 지나가야함
    bottom_idx = bisect.bisect_left(bottom, i)
    # 1,3,5 -> i == 2, h+1-i = 6, 6보다 작은 값 중에 최댓값 인덱스 구하기 -> 3개 다 안부수고 통과 가능
    top_idx = bisect.bisect_left(top, (h + 1 - i))

    # 통과 되는 걸 찾았기 때문에 n에서 그만큼 빼야함
    broken_count = n - (bottom_idx + top_idx)

    # 최솟값이면 최솟값 업데이트
    if broken_count < min_broken_count:
        min_broken_count = broken_count
        range_count = 1

    # 최솟값 가지는 구간 수 1증가
    elif broken_count == min_broken_count:
        range_count += 1


print(min_broken_count, range_count)
