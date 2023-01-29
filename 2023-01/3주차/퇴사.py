"""
dp

뒤에서부터 이 날짜 부터 상담을 시작했을 때 최대 상담 횟수 저장

max(이 날짜에 상담을 할 경우, 이 날짜에 상담을 안할경우)
"""

n = int(input())
schedules = []

d = [0] * (n + 3)

for i in range(n):
    t, p = map(int, input().split())
    schedules.append((t, p))


for day in range(n, 0, -1):
    time, pay = schedules[day - 1]

    next_day = day + time

    # 이 회의를 해도 n+1일날 퇴사할 수 있으면
    if next_day <= n + 1:
        # 이 날짜에 회의를 안 할 경우, 할 경우 중 최댓값
        d[day] = max(d[day + 1], d[next_day] + pay)

    # 못하면 그냥 이전까지의 최댓값
    else:
        d[day] = d[day + 1]

print(d[1])
