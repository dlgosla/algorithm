"""
합병정렬의 swap 개수와 동일

"""
import sys
from collections import deque


def merge_sort(sq):
    # 리스트 길이가 1이 될 때 까지 계속 분할
    if len(sq) <= 1:
        return sq

    mid = len(sq) // 2

    left = sq[:mid]
    right = sq[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    # 끝까지 다 분할했으면 합병시작
    merged = merge(left, right)
    if not merged:
        return []

    return merged


# 합병
def merge(left, right):
    # 합병 후 리스트
    merged = []

    # deque를 이용해 정렬하면서 합병
    right = deque(right)
    left = deque(left)

    while len(right) > 0 and len(left) > 0:
        # 왼쪽과 오른쪽 덱의 첫번 째 요소 크기 비교
        if right[0][1] < left[0][1]:
            merged.append(right.popleft())

        else:
            idx, number = left.popleft()
            merged.append((idx, number))
            print(idx)
            return []

    merged.extend(right)
    merged.extend(left)

    return merged


input = sys.stdin.readline

n = int(input())


sequence = [(i + 1, int(input())) for i in range(n)]

merge_sort(sequence)
