from collections import deque
import copy


def solution(queue1, queue2):
    answer = -2

    len_q1 = len(queue1)
    len_q2 = len(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    # target_sum = (sum1 + sum2) // 2

    count = 0
    while True:
        # temp1 = copy.deepcopy(q1)
        # temp2 = copy.deepcopy(q2)

        if count > (len_q1 + len_q2) * 2:
            return -1

        if sum1 == sum2:
            answer = count
            break

        if q1 and sum1 < sum2:
            elem2 = q2.popleft()
            q1.append(elem2)

            sum1 += elem2
            sum2 -= elem2

        elif q2 and sum >= sum2:
            elem1 = q1.popleft()
            q2.append(elem1)

            sum1 -= elem1
            sum2 += elem1

        count += 1

    return answer


# print(solution([1, 1], [1, 5]))
