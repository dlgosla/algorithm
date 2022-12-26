"""
p 1 0 2
s 0 2 1
{1: [0], 0: [2], 2: [1]})
[0, 2, 1]

if shuffle[i] not in collect_cards[i]:

0번째에 있던 카드는 1에게 가야한다....
섞은거의 1번째가 2이다.. 원래 2번째 있던 게 1로 갔다..
그럼 1번째 사람한테 2가 배정된다는 소리다..
정답을 보자 1번째 사람한테 2가 배정되는 게 맞는가?
p[1]을 보면 0이다. 2가 아니다. 그래서 아니다.


"""

from collections import defaultdict


n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

collect_cards = defaultdict(list)

for i in range(n):
    collect_cards[p[i]].append(i)

init = [i for i in range(n)]
shuffle = init[:]
count = 0
# print(collect_cards)

while True:
    # print(shuffle)

    finish = True
    for i in range(n):
        if shuffle[i] not in collect_cards[i % 3]:
            finish = False

    if finish:
        break

    new_shuffle = shuffle[:]
    for i in range(n):
        new_shuffle[s[i]] = shuffle[i]

    count += 1
    shuffle = new_shuffle[:]

    if init == shuffle:
        count = -1
        break

print(count)
