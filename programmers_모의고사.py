def solution(answers):
    answer = [] # 답을 저장하는 리스트
    first = [1,2,3,4,5] 
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    student = [0,0,0] # 학생이 답을 맞춘 개수 저장
    

    for i in range(len(answers)): #문제 개수만큼 반복
        if answers[i] == first[i % len(first)]:
            student[0] += 1 # 첫번째 학생의 정답개수 증가
            
        if answers[i] == second[i % len(second)]:
            student[1] += 1 # 두번째 학생의 정답개수 증가

        if answers[i] == third[i % len(third)]:
            student[2] += 1# 세번째 학생의 정답개수 증가

    for i in range(3):
        if student[i] == max(student): #현재 학생의 정답 수가 최댓값과 같으면
            answer.append(i+1) #가장 문제를 많이 맞힌 사람이므로 답에 추가(자동으로 오름차순 됨)

    return answer



