def solution(S):
    output = set()
    output.update(S)
    outputList = list(output)
    
    count = 0
    for i in outputList:
        if (S.count(i) % 2) != 0:
            count += 1

    return count


print(solution("acbcbba"))
print(solution("axxaxa"))
print(solution("aaaa"))