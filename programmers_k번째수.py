def solution(array, commands):
    answer = [] #답을 저장할 배열
    
    for i in range(len(commands)): #커맨드 길이만큼 반복 
        low = commands[i][0] #자르기 시작할 위치
        high = commands[i][1] # 자르기를 끝낼 위치
        find = commands[i][2] #찾고 싶은 위치
        splitedAry  = []

        splitedAry = array[low-1:high] #배열을 자름
        splitedAry =  sorted(splitedAry) #정렬
        key = splitedAry[find-1] #정렬한 배열에서 해당 인덱스를 찾음
        answer.append(key) #리턴할 값에 추가
        
    return answer

