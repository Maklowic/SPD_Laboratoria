from RandomNumberGenerator import RandomNumberGenerator


def argmin(p, N, M):
    tmp = 10000
    tmp_j = -1
    tmp_i = -1

    for j in N:
        for i in M:
            if p[j-1][i-1] < tmp:
                tmp = p[j-1][i-1]
                tmp_j = j-1
                tmp_i = i-1
    return [tmp_j, tmp_i]

#
#
#
def Cmax(p, pi, n, m):
    
    C = []

    for j in range(0, n):
        tmp = []
        for i in range(0, m):
            tmp.append(0)
        C.append(tmp)

    # Ustalamy element [0][0] (lewy gorny naroznik)
    C[0][0] = p[pi[0]-1][0]

    for j in range(1, n):  # <--- indeksowanie od 1, ale [1] to drugi element
        C[j][0] = C[j-1][0] + p[pi[j]-1][0]

    for i in range(1, m):  # <- tutaj tez indeksowanie od 1, czyli od drugiego elementu
        C[0][i] = C[0][i-1] + p[pi[0]-1][i]

    for j in range(1, n):      # <- tutaj oba indeksowania od 1 daja poczatek
        for i in range(1, m):  # w elemencie [1][1]
            C[j][i] = max(C[j][i-1], C[j-1][i]) + p[pi[j]-1][i]

    print("C:  ", end='')
    print(C)

    print("Cmax: ", end='')
    print(C[n-1][m-1])

#
#
#
def Johnson(N, M, p, pi):
    # procedura Johnsona
    n = len(N)
    m = len(M)

    l = 0
    k = n-1

    if m == 3:
        inne_p = []
        for j in range(1, n+1):
            tmp = []
            tmp.append(p[j-1][0]+p[j-1][1])
            tmp.append(p[j-1][1]+p[j-1][2])
            inne_p.append(tmp)

        while N:
            j, i = argmin(inne_p, N, [1, 2])

            if inne_p[j][0] < inne_p[j][1]:
                pi[l] = j+1
                l = l+1
            else:
                pi[k] = j+1
                k = k-1
            N.remove(j+1)

    else:
        while N:
            j, i = argmin(p, N, M)

            if p[j][0] < p[j][m-1]:
                pi[l] = j+1
                l = l+1
            else:
                pi[k] = j+1
                k = k-1
            N.remove(j+1)

    print("Po algorytmie Johnsona")
    print("pi: ", end='')
    print(pi)

    return pi

#
#
#
def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj liczbę zadań: "))
    m = int(input("Podaj liczbę maszyn: "))

    problems = range(1, n+1)
    machines = range(1, m+1)

    rng = RandomNumberGenerator(seed)

    J = []
    p = []
    pi = []

    for j in problems:
        J.append(j)
        pi.append(0)
        tmp = []
        for i in machines:
            tmp.append(rng.nextInt(1, 29))
        p.append(tmp)

    print("J:  ", end='')
    print(J)
    print("p:  ", end='')
    print(p)

    # tablica zadań
    N = []
    N = J[:]
    print("N:  ", end='')
    print(N)

    # tablica maszyn
    M = []
    for m in machines:
        M.append(m)
    print("M: ", end='')
    print(M)

    # koniec generowania instancji

    # permutacja po algorytmie Johnsona
    pi = Johnson(N, M, p, pi)

    Cmax(p, pi, n, m)


main()
