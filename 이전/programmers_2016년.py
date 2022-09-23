def solution(a, b):
    answer = ''
    week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0 
    for i in range(a-1):
        days += month[i]
    days += b
    answer = week[(days + 4) % 7 ]
    print(answer)
    return answer

solution(5,24)
