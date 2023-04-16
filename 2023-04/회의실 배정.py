n = int(input())

times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

times.sort()

rooms = []
for i in range(len(times)):
    start_time = times[i][0]
    end_time = times[i][1]

    allocated = False
    for i in range(len(rooms)):
        if rooms[i] <= start_time:
            rooms[i] = end_time
            allocated = True
            break

    if not allocated:
        rooms.append(end_time)

print(len(rooms))
