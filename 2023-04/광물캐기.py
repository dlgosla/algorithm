"""
["diamond", "diamond", "diamond", "iron", "iron", /// "diamond", "iron", "stone"]
5개씩 같이 묶는다

각 구간에서 다이아가 많을수록, 다이아가 같다면 철이 많을 수록 좋은 곡괭이로 캐야 피로도가 줄어든다
=> 

광석을 5개씩 묶고 그 안에서 각 곡괭이로 캤을 때 피로도를 구한다
=> [[85, 17, 5], [31, 7, 3]]] 돌, 철, 다이아 곡괭이

각 구간을 철 곡괭이를 썼을 때 피로도 기준으로 내림차순 정렬 후 각 구간에 최대한 좋은 곡괭이를 배정해주기를 반복한다
=> [[85, 17, 5], [31, 7, 3]]] 돌, 철, 다이아 곡괭이
=> [1, 3, 2] # 다이아 곡괭이 1개, 철 곡괭이 3개, 돌 곡괭이 2개 일 때
=> 첫번 째 구간에서 다이아 곡괭이 사용 [0,3,2] -> 총 피로도 5
=> 두번 째 구간에서 다이아 곡괭이가 없으니 철 곡괭이 사용 [0,2,2] -> 총 피로도 5 + 7 = 12

"""

from heapq import heappush, heappop


def solution(picks, minerals):
    picks.reverse()

    # 돌, 철, 다이아
    pick_fatigue = [[1, 5, 25], [1, 1, 5], [1, 1, 1]]
    mineral_idxs = {"diamond": 2, "iron": 1, "stone": 0}
    fatigues = []
    minerals = minerals[: 5 * sum(picks)]

    while minerals:
        parted_minerals = minerals[:5]
        minerals = minerals[5:]

        curr_fatigue = [0, 0, 0]

        for mineral in parted_minerals:
            mineral_idx = mineral_idxs[mineral]
            for pick_idx in range(3):
                curr_fatigue[pick_idx] -= pick_fatigue[pick_idx][mineral_idx]

        heappush(fatigues, curr_fatigue)

    min_fatigue = 0
    while fatigues:
        fatigue = heappop(fatigues)

        for i in range(2, -1, -1):
            if picks[i]:
                picks[i] -= 1
                min_fatigue += -fatigue[i]
                break

    print(min_fatigue)
    return min_fatigue


solution(
    [1, 3, 2],
    ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"],
)
# solution(
#     [0, 1, 1],
#     [
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#     ],
# )

# solution(
#     [5, 5, 5],
#     [
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "diamond",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#         "iron",
#     ],
# )
