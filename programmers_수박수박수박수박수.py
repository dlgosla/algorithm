def solution(n):
    answer = ''
    pattern = ["수","박"]

    for i in range(n):
        answer += pattern[i%2]
    print(answer)
    return answer

solution(4)
