from RandomNumberGenerator import RandomNumberGenerator

# Minimal value in array
def min_val(a,b):
    tmp = 999
    for i in b:
        if a[i-1] < tmp:
            tmp = a[i-1]
    return tmp

# Index of minimal value in array
def min_idx(a,b):
    tmp = 999
    for i in b:
        if a[i-1] < tmp:
            tmp = a[i-1]
            tmp2 = i
    return tmp2

# Index of maximum value in array
def max_idx(a,b):
    max_tmp = 0
    #tmp = b[0]
    for i in b:
        if a[i-1] > max_tmp:
            max_tmp = a[i-1]
            tmp = i
    return tmp

def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj rozmiar problemu: "))
    problems = range(1, n + 1)

    rng = RandomNumberGenerator(seed)
    J = []
    p = []
    re_p = []
    r = []
    q = []
    G = []
    pi = []
    C = []
    Cq = []
    Cmax = 0

    # Generowanie czasu wykonywania p
    for problem in problems:
        J.append(problem)
        p.append(rng.nextInt(1, 29))

    N = J[:]
    re_p = p
    A = sum(p)
    X = A

    # Generowanie czasu wykonywania
    for problem in problems:
        r.append(rng.nextInt(1, A))

    for problem in problems:
        q.append(rng.nextInt(1, X))

    # Wyświetlenie tablic
    print("J: ", J)
    print("r: ", r)
    print("p: ", p)
    print("q: ", q)

    t = min_val(r,N)
    l=1
    
    while(len(G) > 0 or len(N) > 0):        
        while (N and min_val(r,N) <= t):
            jg = min_idx(r,N)
            G.append(jg)
            N.remove(jg)

        if q[jg-1] > q[l-1]:
            re_p[l-1] = t - r[jg-1]
            t = r[jg-1]
            if re_p[l-1] > 0:
                G.append(l)
                C.pop()
                C.append(t)

        if len(G) > 0:
            jg = max_idx(q, G)             
            l = jg
            pi.append(jg)
            G.remove(jg)
            t = t + re_p[jg - 1]
            C.append(t)
            Cq.append(t+q[jg-1])
            Cmax = max(Cmax, t + q[jg - 1])

        else:
            t = min_val(r,N)

    # Ustalenie wartości wektora c
    #S = [r[pi[0]-1]]
    #C = [S[0] + p[pi[0]-1]]
    #Cq = [C[0] + q[pi[0]-1]]

    #for i in range(1, n):
    #    C.append(max(C[i-1], r[pi[i]-1])+p[pi[i]-1])
    #    Cq.append(C[i] + q[pi[i]-1])

    # Ustalenie wartości wektora S
    #for i in range(1, n):
    #    S.append(max(r[pi[i]-1], C[i-1]))

    print("\nPermutacja po algorytmie Schrage z przerwaniami")
    print("pi: ", pi)
    #print("S: ", S)
    print("C: ", C)
    print("Cq: ", Cq)
    print("Cmax: ", Cmax)


main()