"""
-99 -2 -1 4 98
=> 절댓값 기준으로 정렬
=> -1 -2 4 98 -99
=> 무조건 양옆을 비교하는 게 가장 최솟값일테니 양옆끼리만 비교하면서 가장 최솟값 찾기

"""

n = int(input())
values = [(abs(int(elem)), int(elem)) for elem in input().split()]
values.sort()

answer = []
pre = values[0][1]
min_mix_value = float("inf")
for i in range(1, n):
    abs_v, real_v = values[i]
    curr_mix_value = abs(pre + real_v)

    if curr_mix_value < min_mix_value:
        min_mix_value = curr_mix_value
        answer = [pre, real_v]

    pre = real_v

print(*sorted(answer))
