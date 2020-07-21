def solution(s):
    answer = True
    countP = s.count('p') + s.count('P') #p와 P의 개수를 구해서  더함
    countY = s.count('y') + s.count('Y') #y와 Y의 개수를 구해서  더함

    if countP != countY: # 그 개수가 서로 다르면
        answer = False #false로 바꿈

    return answer


print(solution("ppYy"))
