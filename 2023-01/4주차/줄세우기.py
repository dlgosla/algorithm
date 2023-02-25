"""

증가하는 순으로 배치돼있는 아이들은 냅두고 나머지만 옮기면 된다
=> 증가하는 순으로 배치 된 애들을 최대화 하고 나머지만 옮기면 최소로 옮길 수 있다
=> LIS
=> 전체 아이들 수 - LIS 수

"""

import bisect

n = int(input())
children = []

for i in range(n):
    children.append(int(input()))


dp = []
dp.append(children[0])

# 1 2 5 , 4 -> idx = 2
for child in children:
    # lis의 맨끝 원소보다 지금 원소가 더 크면 맨뒤에 추가
    if dp[-1] < child:
        dp.append(child)

    # 아니면
    else:
        # 이분 탐색으로 이 원소가 들어갈 적절한 위치를 찾아서 대치
        idx = bisect.bisect_left(dp, child)
        dp[idx] = child

print(n - len(dp))
