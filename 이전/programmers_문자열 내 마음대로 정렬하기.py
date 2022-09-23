def solution(strings, n):
    answer = [] 
    tupleList = [] #리스트 안에 튜플
    
    for i in range(len(strings)): #strings의 크기만큼 반복
        tupleList.append((strings[i][n], strings[i])) #튜플을 추가

    # 튜플의 첫번째 요소를 기준으로 정렬하고 
    # 첫번째 요소가 같으면 두번 째 요소로 정렬
    tupleList.sort(key=lambda x:(x[0],x[1]))
    

    for item in tupleList: #튜플리스트에 있는 각각의 튜플에 대하여
        answer.append(item[1]) #튜플의 두번째 값을 answer에 추가

    return answer

solution(["sun", "bed", "car"], 1)
