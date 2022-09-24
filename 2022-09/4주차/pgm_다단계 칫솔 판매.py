# from collections import defaultdict


def solution(enroll, referral, sellers, amounts):
    answer = []

    income = dict.fromkeys(enroll, 0)

    info = {}

    for node, parent in zip(enroll, referral):
        info[node] = parent

    sales = {}
    for seller, amount in zip(sellers, amounts):

        curr_node = seller
        curr_amount = amount * 100

        while True:
            if curr_node == "-":
                break

            parent_node = info[curr_node]
            parent_amount = curr_amount // 10

            if parent_amount < 1:
                income[curr_node] += curr_amount
                break

            income[curr_node] += curr_amount - parent_amount

            curr_amount = parent_amount
            curr_node = parent_node

    # print(income)
    return list(income.values())


print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
    )
)
