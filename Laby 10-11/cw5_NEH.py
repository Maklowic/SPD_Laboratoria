from RandomNumberGenerator import RandomNumberGenerator
import math
UB = 99999

pi_prim = []

#
# indeksy najmniejszej wartości w tablicy p[][]
#


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
# indeksy najwiekszej wartości w tablicy W
#
def argmax(W):
    tmp = 0
    tmp_j = -1

    n = len(W)

    for j in range(1, n+1):
        if W[j-1] > tmp:
            tmp = W[j-1]
            tmp_j = j-1
    return tmp_j


#
# Obliczanie Cmax
#
def Calc_Cmax(p, pi, M):
    n = len(pi)
    m = len(M)

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

    return (C)


#
# procedura Johnsona
#
def Johnson(_N, M, p):
    N = _N[:]
    n = len(N)
    m = len(M)

    pi = []
    for j in range(0, n):
        pi.append(0)

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
# liczenie granicy
#
def Bound(N, M, p, pi):
    m = len(M)
    LEN_PI = len(pi)
    suma_p = 0
    # print("LEN PI:", LEN_PI)
    # print("to pi jest w bound:", pi)

    C = Calc_Cmax(p, pi, M)
    Cmx = C[LEN_PI-1][m-1]

    for idx in N:
        suma_p += p[idx-1][m-1]

    LB = Cmx + suma_p
    # print("LB = ", LB)
    return LB

#
# procedura Branch and Bound
#


def BnB(zad, _N, M, p, pi):
    global UB
    bnb_pi = []
    bnb_pi = pi[:]
    bnb_N = _N[:]
    global pi_prim
    Cmax = 0

    bnb_pi.append(zad)
    bnb_N.remove(zad)
    if bnb_N:
        LB = Bound(bnb_N, M, p, bnb_pi)
        if LB <= UB:
            for k in bnb_N:
                BnB(k, bnb_N, M, p, bnb_pi)
    else:
        C = Calc_Cmax(p, bnb_pi, M)

        Cmax = C[len(bnb_pi)-1][len(M)-1]
        if Cmax <= UB:
            UB = Cmax
            pi_prim = bnb_pi[:]
    # return pi_prim


#
# procedura Brute Force
#
def BruteForce(zad, _N, M, p, pi):
    global UB
    bf_pi = []
    bf_pi = pi[:]
    bf_N = _N[:]

    global pi_prim2

    bf_pi.append(zad)
    bf_N.remove(zad)

    for k in bf_N:
        BruteForce(k, bf_N, M, p, bf_pi)

    C = Calc_Cmax(p, bf_pi, M)
    Cmax = C[len(bf_pi)-1][len(M)-1]
    if Cmax <= UB:
        UB = Cmax
        pi_prim2 = bf_pi[:]
    # return pi_prim


#
# procedura NEH
#
def NEH(N, M, p, pi):
    neh_pi = pi[:]
    neh_N = N[:]
    neh_M = M[:]

    n = len(neh_N)
    m = len(neh_M)

    pig = []
    global pi_prim
    pi_prim_inne = []

    k = 1

    #m = len(M)
    print("p ", p)
    W = []

    for j in neh_N:
        w = 0
        for m in neh_M:
            w += p[j-1][m-1]
        W.append(w)
        print("W ", W)

    while W:
        zad = argmax(W)

        l = 1
        while l <= k:

            pi_prim_inne = pi_prim[:]
            pi_prim_inne.insert(l, zad)

            pi_prim_inne_c = Calc_Cmax(p, pi_prim_inne, neh_M)
            pi_prim_inne_cmax = pi_prim_inne_c[len(pi_prim_inne)-1][m-1]

            if(l == 1):
                pig = pi_prim_inne[:]

            pig_c = Calc_Cmax(p, pig, neh_M)
            pig_cmax = pig_c[len(pig)-1][m-1]

            if pi_prim_inne_cmax < pig_cmax:
                pig = pi_prim_inne[:]
            l += 1

        pi_prim = pig[:]
        maxW = W[zad]
        W.remove(maxW)
        k += 1

#
# main
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
    # print(N)
    # print("N:  ", end='')
    # print(N)

    # tablica maszyn
    M = []
    for m in machines:
        M.append(m)
    # print("M: ", end='')
    # print(M)

    #
    #
    #
    global UB
    global pi_prim
    global pi_prim2
    Johnson_pi = []
    Johnson_pi = Johnson(N, M, p)
    C_john = Calc_Cmax(p, Johnson_pi, M)
    UB = C_john[n-1][m-1]

    print("C:  ", end='')
    print(C_john)

    print("Cmax: ", end='')
    print(C_john[n-1][m-1])
    # print("Ub: ", UB)
    # koniec generowania instancji
    #
    #

    # permutacja po algorytmie Johnsona
    # pi = Johnson(N, M, p, pi)

    '''for zad in N:
        bnb_N = N[:]
        BnB(zad, bnb_N, M, p, pi)

    print("Po algorytmie BnB")
    print("pi: ", end='')
    print(pi_prim)

    C = Calc_Cmax(p, pi_prim, M)
    print("C:  ", end='')
    print(C)

    print("Cmax: ", end='')
    print(C[n-1][m-1])

    for zad in N:
        bnb_N = N[:]
        BruteForce(zad, bnb_N, M, p, pi)

    print("Po algorytmie BF")
    print("pi: ", end='')
    print(pi_prim)

    C = Calc_Cmax(p, pi_prim, M)
    print("C:  ", end='')
    print(C)
    print("Cmax: ", end='')
    print(C[n-1][m-1])'''

    NEH(N, M, p, pi)

    print("Po algorytmie NEH")
    print("pi: ", end='')
    print(pi_prim)

    C = Calc_Cmax(p, pi_prim, M)
    print("C:  ", end='')
    print(C)
    print("Cmax: ", end='')
    print(C[n-1][m-1])


main()
