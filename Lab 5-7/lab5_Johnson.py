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


def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj liczbę zadań: "))
    #m = int(input("Podaj liczbę maszyn: "))

    m = 2
    print("Liczba maszyn: 2")

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

    print("J: ", end='')
    print(J)
    print("p:  ", end='')
    print(p)

    # koniec generowania instancji
    # procedura Johnsona

    l = 0
    k = n-1

    # tablica maszyn
    M = []
    for m in machines:
        M.append(m)

    # tablica zadań
    N = []
    N = J[:]
    print("N: ", end='')
    print(N)
    # permutacja

    #tmp = argmin(p, N, M)
    # print(tmp)

    while N:
        j, i = argmin(p, N, M)

        if p[j][0] < p[j][1]:
            pi[l] = j+1
            l = l+1
        else:
            pi[k] = j+1
            k = k-1
        N.remove(j+1)

    print("Po algorytmie Johnsona")
    print("pi: ")
    print(pi)


main()
