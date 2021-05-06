from RandomNumberGenerator import RandomNumberGenerator
import time
import math

#
# Zmienne globalne
#
F_min = 999999999
pi_prim2 = []
T_glob = []
C_glob = []
wT_glob = []
memory_glob=[]

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
# czyszczenie bitów
#
def bit_clear(val, bit):
    return val & ~(1 << bit)

#
# Programowanie dynamiczne - iteracyjne
#
def PD(J, p, d, w, pi):
    # definicje
    n = len(J)
    _infinity = math.inf
    pow_n = pow(2, n)
    D = range(1, pow_n)
    memory = [0] * pow_n
    min_arg = [0] * pow_n

    for i in D:
        _bin = [int(bit) for bit in bin(i)[2:]]
        _bin.reverse()
        inne_D = [bit for bit, val in enumerate(_bin) if val]
        sum_p = 0
        memory[i] = _infinity

        for j in inne_D:
            sum_p = sum_p + p[j]

        for j in inne_D:
            bit = bit_clear(i, j)
            val = max(sum_p - d[j], 0) * w[j] + memory[bit]

            if val < memory[i]:
                memory[i] = val
                min_arg[i] = j + 1

    pi.append(min_arg[pow_n - 1])
    bit = pow_n - 1
    for _ in range(n-1):
        bit = bit_clear(bit, pi[-1]-1)
        pi.append(min_arg[bit])

    pi.reverse()
    
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
    bit = A

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

    D=J[:]

    global T_glob
    global C_glob
    global wT_glob
    # koniec generowania instancji
    #
    #

    start_time2 = time.time()
    PD(J, p, d, w, pi)
    tmp_time2 = time.time() - start_time2

    F = Calc_Fmin(p, pi, d, w)
    print("!!!! po algorytmie PD")
    print("pi: ", pi)
    print("C: ", C_glob)
    print("T: ", T_glob)
    print("wT: ", wT_glob)
    print("F: ", F)
    print("Czas działania: %.5s s" % tmp_time2)
    
    print("\n           Key to continue . . .")
    input()
main()
