from itertools import permutations


def solution(k, dungeons):
    answer = -1

    # dungeons = [ (required, consume) for required, consume in dungeons]
    # print(dungeons)

    combs = permutations(dungeons, len(dungeons))
    max_explore_count = 0
    for comb in combs:
        curr_explore_count = 0
        remained_fatigue = k
        for required, consume in comb:
            if required <= remained_fatigue:
                remained_fatigue -= consume
                curr_explore_count += 1
            else:
                continue

        if max_explore_count < curr_explore_count:
            max_explore_count = curr_explore_count

    return max_explore_count
