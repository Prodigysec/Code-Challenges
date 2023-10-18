def solution(S):
    fragments = []

    for i in range(len(S)-1):
        fragment = int(S[i:i+2])
        fragments.append(fragment)

    fragments.sort(reverse=True)

    largestSum = 0
    i = 0

    while i < len(fragments):
        largestSum += fragments[i]
        i += 2

    return largestSum

print(solution("43798"))
print(solution("00101"))
print(solution("0332331"))
print(solution("00331"))