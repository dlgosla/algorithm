from datetime import datetime, timedelta


def solution(book_times):
    answer = 0

    book_times.sort()
    rooms = []

    for [start, end] in book_times:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        # print(start_time, end_time, (end_time - start_time))

        allocated = False
        for i in range(len(rooms)):
            if rooms[i] <= start_time:
                rooms[i] = end_time + timedelta(minutes=10)
                allocated = True
                break

        if not allocated:
            rooms.append(end_time + timedelta(minutes=10))

    # print(rooms)

    return answer


solution(
    [
        ["15:00", "17:00"],
        ["16:40", "18:20"],
        ["14:20", "15:20"],
        ["14:10", "19:20"],
        ["18:20", "21:20"],
    ]
)
