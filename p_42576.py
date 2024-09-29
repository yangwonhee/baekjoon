## 1st solution (sort -> )
def solution1(participant, completion):
    # 1. sorting 
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]


## 2nd solution (hash)
def solution2(participant, completion):
    hash_dict = {}
    hash_sum = 0
    for part in participant:
        hash_dict[hash(part)] = part
        hash_sum += hash(part)
    for i in completion:
        hash_sum -= hash(i)
    return hash_dict[hash_sum]

from collections import Counter
def solution3(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]

print(solution3(["leo", "kiki", "eden"], ["eden", "kiki"]))
