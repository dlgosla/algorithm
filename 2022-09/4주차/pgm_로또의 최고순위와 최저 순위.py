def calc_rank(count):
    return 6 if count < 2 else 7 - count


def solution(lottos, win_nums):
    answer = []

    zero_count = 0
    win_count = 0

    for lotto in lottos:
        if lotto in win_nums:
            win_count += 1

        elif lotto == 0:
            zero_count += 1

    min_rank = calc_rank(win_count)
    max_rank = calc_rank(win_count + zero_count)

    answer = [max_rank, min_rank]

    return answer
