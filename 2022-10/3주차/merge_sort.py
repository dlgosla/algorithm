from collections import deque


def divide(lst):
    length = len(lst)

    if length == 1:
        return lst

    mid = length // 2

    # left = lst[:mid]
    # right = lst[mid:]

    left = divide(lst[:mid])
    right = divide(lst[mid:])

    # divide(left)
    # divide(right)

    merged_lst = merge(left, right)

    return merged_lst


def merge(left, right):

    left = deque(left)
    right = deque(right)

    merged_lst = []

    while left and right:
        e1 = left[0]
        e2 = right[0]

        if e1 < e2:
            merged_lst.append(e1)
            left.popleft()

        else:
            merged_lst.append(e2)
            right.popleft()

    merged_lst.extend(left)
    merged_lst.extend(right)

    return merged_lst


print(divide([3, 2, 4, 1, 2, 6]))
