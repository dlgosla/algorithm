from collections import defaultdict


def solution(id_list, reports, k):
    answer = []

    report_dicts = defaultdict(set)

    for report in reports:
        reporting, reported = report.split()

        report_dicts[reported].add(reporting)

    msgs = dict.fromkeys(id_list, 0)
    for reported, reportings in report_dicts.items():

        if len(reportings) >= k:
            msgs[reported] += 1

            for reporting in reportings:
                msgs[reporting] += 1

    # print(msgs)

    return list(msgs.values())


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
)
