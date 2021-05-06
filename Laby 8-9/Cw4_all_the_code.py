from RandomNumberGenerator import RandomNumberGenerator
import time

#
# Zmienne globalne
#
F_min = 999999999
pi_prim2 = []
T_glob = []
C_glob = []
wT_glob = []

#
# Obliczanie wiTi
#
def Calc_Fmin(p, pi, d, w):
    global T_glob
    global C_glob
    global wT_glob
    n = len(pi) 
    C = []
    T = []
    wT = []
    for j in range(0, n):
        C.append(0)
        T.append(0)
        wT.append(0)

    C[0] = p[pi[0]-1]
    for j in range(1, n):
        C[j] = C[j-1] + p[pi[j]-1]
    C_glob = C[:]
    
    for k in range(0, n):
        T[k] = max( (C[k] - d[pi[k]-1]), 0)
    T_glob = T[:]
    #print("To jest T", T)
    for i in range(0, n):
        wT[i] = w[pi[i]-1]*T[i]
    wT_glob = wT[:]
    F = sum(wT)
    #print("return F: ", F)
    return F

#
# procedura Brute Force
#
def BruteForce(zad, _N, p, pi, d, w):
    #global iteracje
    #iteracje = iteracje+1
    #print(iteracje)
    #print("zad: ", zad)
    bf_N = []
    bf_N = _N[:]
    bf_pi = []
    bf_pi = pi[:]
    global F_min
    global pi_prim2
        
    bf_pi.append(zad)
    bf_N.remove(zad)

    for k in bf_N:
        BruteForce(k, bf_N, p, bf_pi, d, w)
    #print("pi ", bf_pi)
    
    if len(bf_pi) == len(p):
        F_inne = Calc_Fmin(p, bf_pi, d, w)
        if F_inne < F_min:
            F_min = F_inne
            pi_prim2 = bf_pi[:]

#
# procedura Greedy
#
def Greedy(d):
    n = len(d)
    pi = []
    tmp = d[:]
    tmp.sort()
    while tmp:
        for k in range(0, n):
            if tmp[0] == d[k]:
                pi.append(k+1)
                tmp.remove(d[k])
                if len(tmp) == 0:
                    return pi


#
# main
# 
def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj liczbę zadań: "))

    problems = range(1, n+1)

    rng = RandomNumberGenerator(seed)

    J = []
    p = []
    pi = []
    w = []
    d = []

    for j in problems:
        J.append(j)
        #pi.append(0)
        p.append(rng.nextInt(1, 29))

    print("J:  ", end='')
    print(J)
    print("p:  ", end='')
    print(p)

    A = sum(p)
    X = A

    # Generowanie czasu wykonywania
    for problem in problems:
        w.append(rng.nextInt(1, 9))

    for problem in problems:
        d.append(rng.nextInt(1, 29))

    print("d:  ", end='')
    print(d)
    print("w:  ", end='')
    print(w)
    # tablica zadań
    N = []
    N = J[:]

    global T_glob
    global C_glob
    # koniec generowania instancji
    #
    #

    
    start_time = time.time()
    
    pi_greedy = Greedy(d)

    tmp_time = time.time() - start_time
    F = Calc_Fmin(p, pi_greedy, d, w)
    print("!!!! po algorytmie Greedy")
    print("pi: ", pi_greedy)
    print("C: ", C_glob)
    print("T: ", T_glob)
    print("wT: ", wT_glob)
    print("wiTi = F: ", F)
    print("Czas działania: %.5s s" % tmp_time)

    start_time2 = time.time()
    for zad in N:
        bf_N = N[:]
        BruteForce(zad, bf_N, p, pi, d, w)
    
    tmp_time2 = time.time() - start_time2

    #pi_z_zajec = [2, 5, 1, 7, 4, 8, 3, 6]
    #pi_z_zajec = [2, 5, 7, 3, 8, 6, 4, 1]
    #pi_z_zajec = [1, 2, 3, 4, 5,6,7,8]

    F = Calc_Fmin(p, pi_prim2, d, w)
    print("!!!! po algorytmie Brute Force")
    print("pi: ", pi_prim2)
    print("C: ", C_glob)
    print("T: ", T_glob)
    print("wT: ", wT_glob)
    print("F: ", F)
    
    print("Czas działania: %.5s s" % tmp_time2)
    
    print("\n           Key to continue . . .")
    input()
    
main()
