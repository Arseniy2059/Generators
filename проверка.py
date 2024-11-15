def iterate(S):
    for i in range(len(S)+1):
        if i == 0:
            yield(S[0:0])
        else:
            for j in range(len(S)-i+1):
                yield(S[j:j+i])


for s in iterate('ABCDEFGHI'):
    print(s)
