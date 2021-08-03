
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion):
        if i != j:
            print(i)
            return i
    print(participant[-1])
    return participant[-1]


solution(["leo", "kiki", "eden"],
         ["eden", "kiki"])
