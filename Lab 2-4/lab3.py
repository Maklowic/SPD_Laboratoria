from RandomNumberGenerator import RandomNumberGenerator


def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj rozmiar problemu: "))
    problems = range(1, n + 1)

    rng = RandomNumberGenerator(seed)
    J = []
    p = []
    r = []
    q = []
    G = []
    pi = []
    Cmax = 0
    l=0

    # Generowanie czasu wykonywania p
    for problem in problems:
        J.append(problem)
        p.append(rng.nextInt(1, 29))

    N = J[:]
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

    min_r = r[0]
    for i in N:
        if r[i-1] < min_r:
            min_r = r[i-1]
    t = min_r

    #tab = [10, 0, 0, 10000]  # nr r p q
    
    #Cmax = t + p[jg-1]
    
    while(len(G) > 0 or len(N) > 0):
        for i in N:
            if r[i-1] <= t:
                G.append(i)
                N.remove(i)
                if q[i-1] > q[l-1]:
                    p[l-1] = t - r[i-1]
                    t = r[i-1]
                    if p[l-1] > 0:
                        G.append(l)
        if len(G) > 0:
            jg = G[0]
            max_qG = q[jg-1]
            for i in G:
                if q[i-1] > max_qG:
                    max_qG = q[i-1]
                    jg = i                    
            l = jg
            pi.append(jg)
            G.remove(jg)
            t += p[jg - 1]
            Cmax = max(Cmax, t + q[jg - 1])

        else:
            jg = N[0]
            min_r = r[jg - 1]
            for i in N:
                if r[i-1] < min_r:
                    min_r = r[i-1]

            t = min_r

    # Ustalenie wartości wektora c
    S = [r[pi[0]-1]]
    C = [S[0] + p[pi[0]-1]]
    Cq = [C[0] + q[pi[0]-1]]

    for i in range(1, n):
        C.append(max(C[i-1], r[pi[i]-1])+p[pi[i]-1])
        Cq.append(C[i] + q[pi[i]-1])

    # Ustalenie wartości wektora S
    for i in range(1, n):
        S.append(max(r[pi[i]-1], C[i-1]))

    print("\nKolejność po algorytmie Schrage z przerwaniami")
    print("pi: ", pi)
    print("S: ", S)
    print("C: ", C)
    print("Cq: ", Cq)
    print("Cmax: ", Cmax)


main()