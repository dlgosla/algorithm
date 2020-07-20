import collections

def solution(participant, completion):
    answer = ''
    countParticipant = collections.Counter(participant)
    countCompletion = collections.Counter(completion)

    for i in range(len(participant)):
        key = participant[i]
        if countParticipant[key] != countCompletion[key]:
            answer = key
            return answer
            
    
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
