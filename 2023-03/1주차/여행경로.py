from collections import defaultdict, deque


def solution(tickets):
    answer = []

    sorted_tickets = sorted(tickets, reverse=True)

    ticket_dict = defaultdict(list)
    for [departure, destination] in sorted_tickets:
        ticket_dict[departure].append(destination)

    dq = deque(["ICN"])

    while dq:
        departure = dq[-1]

        if ticket_dict[departure]:
            destination = ticket_dict[departure].pop()
            dq.append(destination)
        else:
            answer.append(dq.pop())

    # print(answer)
    return answer[::-1]


# print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
