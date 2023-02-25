from itertools import combinations


def solution(relation):
    answer = 0

    row_len = len(relation)
    col_len = len(relation[0])

    combs = [[] for _ in range(col_len + 1)]
    for i in range(row_len):
        for j in range(1, col_len + 1):
            combs[j].append((list(combinations(relation[i], j))))

    print(combs)

    return answer


solution(
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
)
