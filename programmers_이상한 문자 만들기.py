def solution(s):
    answer = ''
    trans = [] 
    for word in s.split(): # 공백을 기준으로 문자열을 나눠서
        word = list(word) # 값 변경을 위해 리스트로 바꾸고
        for i in range(len(word)): # 각 word길이만큼
            if i % 2 == 0: # 짝수면
                word[i] = word[i].upper() #대문자로
            else: #홀수면  
                word[i] = word[i].lower() #소문자로 바꿔서
        trans.extend(word) # trans에 이어 붙인다
        trans.append(" ") #공백 추가
                         
    answer = "".join(trans).strip() # 앞뒤 공백 제거
    return answer

