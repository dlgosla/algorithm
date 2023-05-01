"""
완탐은 안되겠고 그리디
-> 무조건 작업량 높은 거 부터 처리

"""


from heapq import heappop, heappush


def solution(n, works):
    answer = 0

    hq = []
    for work in works:
        heappush(hq, -work)

    for i in range(n):
        work = -heappop(hq)

        if work == 0:
            break

        work -= 1
        heappush(hq, -work)

    for work in hq:
        work = -work
        answer += work**2

    return answer


# print(solution(4, [4, 3, 3]))
# print(solution(3, [1, 1]))
