def plus_grande_sequence(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    times = [int(line.strip()) for line in lines]

    
    P = [ -1 for i in range(len(times))]
    M = [ -1 for i in range(len(times)+1)]

    L = 0

    for i in range(len(times)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo+hi)//2
            if times[M[mid]] > times[i]:
                lo = mid+1
            else:
                hi = mid-1
        newL = lo
        P[i] = M[newL-1]
        M[newL] = i

        if newL > L:
            M[newL] = i
            L = newL
        elif times[i] > times[M[newL]]:
            M[newL] = i

    S = [-1 for i in range(L)]
    k = M[L]
    for i in range(L-1, -1, -1):
        S[i] = k
        k = P[k]

    with open('result.txt', 'w') as f:
        f.write(" ".join(map(str, [times[i] for i in S])))

    return S

longest_progression = plus_grande_sequence("data.txt")