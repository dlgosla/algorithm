"""
무적권은 지나온 라운드에서 가장 많은 적이 나왔던 라운드에서 사용해야 매우 효과적이다.
무적권을 사용하면, 병사의 수가 차감되지 않는다.
=> 막히는 순간이 오면 무적권이 남아 있는지 보고 그 이전에 적군이 많았던 턴을 무적권으로 대체

"""


from heapq import heappop, heappush, heappushpop


def solution(n, k, enemy):
    answer = 0
    hq = []

    for curr_enemy in enemy:

        # 병사가 현재 적군 수 보다 적다면
        if n < curr_enemy:
            # 무적권 사용할 수 있으면 대체
            if k > 0:
                max_num = -heappushpop(hq, -curr_enemy)
                n += max_num
                n -= curr_enemy
                k -= 1

            # 못하면 끝
            else:
                break
        else:
            heappush(hq, -curr_enemy)
            n -= curr_enemy

        answer += 1

    return answer


# # solution(7, 3, [4, 2, 4, 5, 3, 3, 1])
# # print(solution(2, 2, [7, 1, 2]))
# # solution(2, 4, [3, 3, 3, 3])
