from RandomNumberGenerator import RandomNumberGenerator
import math
import time

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
# Indeks największej wartości w tab. W_inne w zapisie tab. W
# Problem:
#   usuwanie bezpośrednie z tablicy W powoduje zmniejszenie tablicy
#   przez co indeks nie będzie n tylko mniejszy, bo tablica się 
#   zmniejsza z każdym wykonaniem
#
def argmax_W(W_inne, W):
    tmp_j = -1

    n = len(W)

    # max aktualnej tablicy W
    max_W_inne = max(W_inne)

    for j in range(1, n+1):
        if W[j-1] == max_W_inne:
            tmp_j = j
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
# Ścieżka krytyczna
#
def Crit_patch(p, pi, C, M):
    n = len(pi)
    m = len(M)
    pmax_p = -1
    pmax_m = -1
    tmp_pmax = -1
    idx_p = 0
    idx_m = 0

    path_len = n + m - 1
    
    #print("C: ",C)
    CP = C[idx_p][idx_m]
    i = 1
    while i < path_len:
        if (idx_p == n-1) and (idx_m == m-1):
            # print("idx_p ", idx_p)
            # print("idx_m ", idx_m)
            # print("")
            if tmp_pmax < p[idx_p][idx_m]:
                tmp_pmax = p[idx_p][idx_m]
                pmax_p = idx_p
                pmax_m = idx_m

        elif(idx_m == m-1):
            idx_p += 1
            # print("idx_p ", idx_p)
            # print("idx_m ", idx_m)
            # print("")
            if tmp_pmax < p[idx_p][idx_m]:
                tmp_pmax = p[idx_p][idx_m]
                pmax_p = idx_p
                pmax_m = idx_m
        
        elif(idx_p == n-1):
            # print("idx_p ", idx_p)
            # print("idx_m ", idx_m)
            # print("")
            idx_m += 1
            if tmp_pmax < p[idx_p][idx_m]:
                tmp_pmax = p[idx_p][idx_m]
                pmax_p = idx_p
                pmax_m = idx_m

        else:
            #print("idx_p ", idx_p)
            #print("idx_m ", idx_m)
            #print("")
            if C[idx_p + 1][idx_m] > C[idx_p][idx_m + 1]:
                idx_p += 1
                if tmp_pmax > p[idx_p][idx_m]:
                    tmp_pmax = p[idx_p][idx_m]
                    pmax_p = idx_p
                    pmax_m = idx_m
            
            else:
                idx_m += 1
                if tmp_pmax < p[idx_p][idx_m]:
                    tmp_pmax = p[idx_p][idx_m]
                    pmax_p = idx_p
                    pmax_m = idx_m
        
        i+=1

    return [pmax_p, pmax_m]


#
# Faza II alg. NEH - 
# Zadanie zawierajace najdłuzsza operacje na sciezce krytycznej.
#
def Phase2_crit_path(p, pi, M):
    neh_M = M[:]
    phase2_pi = pi[:]
    m = len(neh_M)
    C = Calc_Cmax(p, pi, M)
    idx_p, idx_m = Crit_patch(p, pi, C, M)
    idx_phase2 = pi[idx_p-1]

    print("faza 2: ", idx_phase2)
    phase2_pi.remove(idx_phase2)
    inne_l = 1
    while inne_l <= len(phase2_pi)+1:
        # przypisywanie wartości na L miejsce
        phase2_pi_inne = phase2_pi[:]
        # insert umieszcza na wybranej pozycji
        phase2_pi_inne.insert(inne_l-1, idx_phase2)
        phase2_pi_inne_c = Calc_Cmax(p, phase2_pi_inne, neh_M)
        phase2_pi_inne_cmax = phase2_pi_inne_c[len(phase2_pi_inne)-1][m-1]
        if(inne_l == 1):
            pig_inne = phase2_pi_inne[:]

        pig_inne_c = Calc_Cmax(p, pig_inne, neh_M)
        pig_inne_cmax = pig_inne_c[len(pig_inne)-1][m-1]

        # Sprawdzenie które podsawienie będzie najlepsze
        if phase2_pi_inne_cmax < pig_inne_cmax:
            pig_inne = phase2_pi_inne[:]
        inne_l += 1
        print("             ", phase2_pi_inne)
        print("             ", phase2_pi_inne_c[len(phase2_pi_inne)-1][m-1])

    return pig_inne


#
# Faza II alg. NEH. - 
# Zadanie, którego usuniecie spowoduje najwieksze zmniejszenie wartosci Cmax
#
def Phase2_Cmax(p, pig, zad, neh_M):
    tmp_Cmax = 99999999999999
    idx_phase2 = -1
    phase2_pi = pig[:]

    m = len(neh_M)
    for i in phase2_pi:
        pig_inne = phase2_pi[:]
        if i != zad:
            pig_inne.remove(i)
            Cmax = Calc_Cmax(p, pig_inne, neh_M)
            if Cmax[len(pig_inne)-1][m-1] < tmp_Cmax:
                tmp_Cmax = Cmax[len(pig_inne)-1][m-1]
                idx_phase2 = i
                # print("faza 2: ", idx_phase2)
    if idx_phase2 > 0:
        #print("faza 2: ", idx_phase2)
        phase2_pi.remove(idx_phase2)
        inne_l = 1
        while inne_l <= len(phase2_pi)+1:
            # przypisywanie wartości na L miejsce
            phase2_pi_inne = phase2_pi[:]
            # insert umieszcza na wybranej pozycji
            phase2_pi_inne.insert(inne_l-1, idx_phase2)

            phase2_pi_inne_c = Calc_Cmax(p, phase2_pi_inne, neh_M)
            phase2_pi_inne_cmax = phase2_pi_inne_c[len(phase2_pi_inne)-1][m-1]

            if(inne_l == 1):
                pig_inne = phase2_pi_inne[:]

            pig_inne_c = Calc_Cmax(p, pig_inne, neh_M)
            pig_inne_cmax = pig_inne_c[len(pig_inne)-1][m-1]

            # Sprawdzenie które podsawienie będzie najlepsze
            if phase2_pi_inne_cmax < pig_inne_cmax:
                pig_inne = phase2_pi_inne[:]
            inne_l += 1
            # print("             ", phase2_pi_inne)
            # print("             ", phase2_pi_inne_c[len(phase2_pi_inne)-1][m-1])

    return pig_inne



#
# procedura NEH
#
def NEH(N, M, p):
    neh_N = N[:]
    neh_M = M[:]

    n = len(neh_N)
    m = len(neh_M)

    pig = []
    pi_prim = []
    pi_prim_inne = []

    k = 1

    W = []

    for j in neh_N:
        w = 0
        for m in neh_M:
            w += p[j-1][m-1]
        W.append(w)
    print("W: ", W)

    W_inne = W[:]
    kolej_W = []
    while W_inne:
        zad = argmax_W(W_inne, W)
        kolej_W.append(zad)
        maxW = W[zad-1]
        W_inne.remove(maxW)
    print(kolej_W)
    print("")
    
    W_inne = W[:]
    while W_inne:
        # indeks najwiekszego W
        zad = argmax_W(W_inne, W)
        l = 1
        # faza 1
        while l <= k:
            # przypisywanie wartości na L miejsce
            pi_prim_inne = pi_prim[:]
            # insert umieszcza na wybranej pozycji
            pi_prim_inne.insert(l-1, zad)

            pi_prim_inne_c = Calc_Cmax(p, pi_prim_inne, neh_M)
            pi_prim_inne_cmax = pi_prim_inne_c[len(pi_prim_inne)-1][m-1]

            if(l == 1):
                pig = pi_prim_inne[:]

            pig_c = Calc_Cmax(p, pig, neh_M)
            pig_cmax = pig_c[len(pig)-1][m-1]

            # Sprawdzenie które podsawienie będzie najlepsze
            if pi_prim_inne_cmax < pig_cmax:
                pig = pi_prim_inne[:]
            l += 1
            # print(pi_prim_inne)
            # print(pi_prim_inne_c[len(pi_prim_inne)-1][m-1])
        #faza 2
        # if(len(pig) != 1):
        #     Phase2_crit_path(p, pig, M)
        pig = Phase2_Cmax(p, pig, zad, neh_M)

        pi_prim = pig[:]
        print("best: ", pi_prim)
        maxW = W[zad-1]
        # usunięcie wstawionego zadania
        W_inne.remove(maxW)
        k += 1
    return pi_prim

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

    # tablica maszyn
    M = []
    for m in machines:
        M.append(m)
    #
    #  koniec generowania instancji
    #

    #
    #  
    #
    Johnson_pi = []
    start_time = time.time()

    Johnson_pi = Johnson(N, M, p)
    tmp_time = time.time() - start_time

    C_john = Calc_Cmax(p, Johnson_pi, M)

    print("C:  ", end='')
    print(C_john)

    print("Cmax: ", end='')
    print(C_john[n-1][m-1])
    print("Czas działania: %.5s s" % tmp_time)

    NEH_pi = []
    start_time2 = time.time()
    NEH_pi = NEH(N, M, p)
    tmp_time2 = time.time() - start_time2

    print("Po algorytmie NEH")
    print("pi: ", end='')
    print(NEH_pi)

    NEH_C = Calc_Cmax(p, NEH_pi, M)
    print("C:  ", end='')
    print(NEH_C)
    print("Cmax: ", end='')
    print(NEH_C[n-1][m-1])
    print("Czas działania: %.5s s" % tmp_time2)

    print("\n           Key to continue . . .")
    input()

main()
