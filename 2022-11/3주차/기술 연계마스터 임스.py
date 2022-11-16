"""
1~9 -> 그냥 발동
R -> L이 있으면 발동
K -> S가 있으면 발동
-> 본 기술이 들어왔을 때 바로 전에 사전 기술이 쓰였는 지 알아야한다. 
-> 스택

중간에 다른 기술이 있어도 상관없음 (SLKR 이어도 다 발동됨)
-> SK와 LR을 별개로 생각
-> 스택 두개

본 기술이 들어왔을 때 각 스택에서 제일 최근에 사전 기술이 사용됐는 지 보고 
사용됐으면 넘어가고 안됐으면 멈추는 방법

"""

from collections import deque
from curses.ascii import isdigit

n = int(input())
skils = input()

LRstack = deque()
SKstack = deque()

# 본기술 : 스택
stack = {
    "L": LRstack,
    "S": SKstack,
    "R": LRstack,
    "K": SKstack,
}

# 본기술: 사전기술
pre_skils = {
    "R": "L",
    "K": "S",
}

count = 0
for skil in skils:
    if isdigit(skil):
        count += 1

    # 본기술이면 사전기술이 있는 지 보고 있으면 count증가
    elif skil in pre_skils.keys():
        if stack[skil] and (stack[skil][-1] == pre_skils[skil]):
            count += 1
            stack[skil].pop()
        else:
            break

    # 사전기술이면 스택에 추가
    else:
        stack[skil].append(skil)


print(count)
