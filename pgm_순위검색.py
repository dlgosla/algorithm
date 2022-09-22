from collections import Counter, defaultdict

from itertools import combinations


def solution4(info, query):
    answer = []

    info_hash = defaultdict(list)

    for i in info:
        splited_info = i.split()
        score = splited_info.pop()
        for r in range(5):
            combs = combinations(range(4), r)

            for comb in combs:
                key = splited_info[:]
                for elem in comb:
                    key[elem] = "-"

                info_hash[" ".join(key)].append(int(score))

    for item in info_hash:
        info_hash[item].sort()

    print(info_hash)

    for q in query:
        splited_q = q.replace(" and", "").split()
        target_score = int(splited_q.pop())

        target_key = " ".join(splited_q)

        matched_score_list = info_hash[target_key]

        if not matched_score_list:
            answer.append(0)
            continue

        score_len = len(matched_score_list)

        start = 0
        end = score_len
        mid = (start + end) // 2

        while start < end:
            mid = (start + end) // 2

            mid_score = matched_score_list[mid]

            if mid_score < target_score:
                start = mid + 1

            else:
                end = mid

        answer.append(score_len - start)

    return answer


def solution2(info, query):
    answer = []

    scores = {}
    stacks = []
    queries = []

    for mem, i in enumerate(info):
        splited = i.split()
        score = splited.pop()

        stacks.append(splited)
        scores[mem] = int(score)

    for q in query:
        queries.append(q.replace(" and", "").split())

    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for q in queries:
        min_score = int(q.pop())
        filtered = []

        for mem, score in scores:
            if score < min_score:
                break
            filtered.append(mem)

        for idx, curr_q in enumerate(q):
            if curr_q == "-":
                continue

            temp = []
            for mem in filtered:
                condition = stacks[mem][idx]

                if condition == curr_q:
                    temp.append(mem)

            filtered = temp

        answer.append(len(filtered))

    return answer


def solution3(info, query):
    answer = []

    info_hash = {}
    scores = {}

    for member, info_string in enumerate(info):
        for idx, info_word in enumerate(info_string.split()):
            if idx == 4:
                scores[member] = int(info_word)
                continue

            if info_hash.get(info_word):
                info_hash[info_word].append(member)

            else:
                info_hash[info_word] = [member]

    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    # print(info_hash)
    # print(scores)

    for q in query:
        splited_q = q.replace(" and", "").split()
        min_score = int(splited_q.pop())
        answer_count = 5

        matched = []
        for member, score in scores:
            if score < min_score:
                break
            matched.append(member)

        # print(matched, "init")

        for q_elem in splited_q:
            if q_elem == "-":
                answer_count -= 1
                continue

            # print(q_elem, matched, info_hash.get(q_elem, []))
            matched.extend(info_hash.get(q_elem, []))

        matched_counts = Counter(matched)
        # matched_counts = sorted(
        #     matched_counts.items(), key=lambda x: x[1], reverse=True
        # )

        # print(matched_counts)

        temp_count = 0
        for member, matched_count in matched_counts:
            if matched_count == answer_count:
                temp_count += 1

        answer.append(temp_count)

    return answer


def solution(info, query):
    # info : 지원자 정보
    # query : 조건
    # [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

    answer = []

    # 쿼리 개수 만큼 반복
    for i in range(len(query)):
        count = 0

        # java and backend and junior and pizza 100 = > ['java', 'backend', 'junior', 'pizza', '100']
        q = query[i].split(" and ")
        last = q[-1].split(" ")
        q.pop()
        q = q + last

        # 각 유저에 대해서
        for data in info:
            for j in range(len(q)):
                # 이 쿼리의 모든 조건을 만족하면 count를 늘림
                if j == 4:
                    if int(q[j]) <= int(data.split()[-1]):
                        count += 1

                if q[j] == "-":
                    continue

                # 하나라도 조건에 안맞는 유저면 버림
                elif j != 4 and data.find(q[j]) == -1:
                    break

        answer.append(count)

    return answer


a = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]

b = [
    "java and backend and junior and pizza 400",
    "python and frontend and senior and chicken 200",
    # "cpp and - and senior and pizza 250",
    # "- and backend and senior and - 150",
    # "- and - and - and chicken 100",
    # "- and - and - and - 150",
]
# print(solution(a, b))
# print()
# print(solution2(a, b))
print(solution4(a, b))
