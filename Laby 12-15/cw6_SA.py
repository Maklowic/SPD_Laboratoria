from RandomNumberGenerator import RandomNumberGenerator
import math
import time
from random import randint
from random import random
from cw6_inne import *

# 
# Funkcja do zmiany pozycji dwoch elementow tablicy
#
def swap(tablica, pos1, pos2):
    tablica[pos1], tablica[pos2] = tablica[pos2], tablica[pos1]
    return tablica

#
# Funkcja do obliczania prawdopodobienstwa akceptacji w algorytmie
# symulowanego wyzarzania
#
#       p = e^( delta_Cmax / T ), gdzie delta_Cmax = Cmax(pi) - Cmax(new_pi)
def Calc_prob(Cmax, Cmax_new, T):
    prob = math.e ** ((Cmax - Cmax_new) / T)
    return prob



#
# Funkcja do obliczania obniżonej temperatury
#
#       Wykorzystane obnizanie temperatury to logarytmiczne
#       T' = T / ln(it+1), gdzie it - nr iteracji algorytmu
def ReduceTemperature(T, it):
    red_T = (T / math.log(it + 1))
    return red_T


#
# SYMULOWANE WYŻARZANIE
#

def simuAnnealing(liczba_zadan, liczba_maszyn, tablica_p, tablica_N, tablica_M, temperatura, temp_koncowa, il_iteracji):
    sa_n = liczba_zadan
    sa_m = liczba_maszyn
    sa_p = tablica_p[:]
    sa_N = tablica_N[:]
    sa_M = tablica_M[:]
    sa_T = temperatura
    # Jaka ustawic temperature koncowa?
    #T_end = sa_T - 30
    T_end = temp_koncowa
    sa_L = il_iteracji
    sa_pi = []
    sa_final_pi = []
    sa_prob = 999999

    # wstepne naszykowanie permutacji jako permutacja naturalna
    for problem in range(1, sa_n+1):
        sa_pi.append(problem)

        sa_final_pi.append(problem)

    # prawdopodobienstwo akceptacji
    # p = e^( delta_Cmax / T ), gdzie delta_Cmax = Cmax(pi) - Cmax(new_pi)

    # Wykorzystane obniżanie temperatury to logarytmiczne
    # T' = T / ln(it+1), gdzie it - nr iteracji algorytmu

    while sa_T > T_end:
        for k in range(1, sa_L):
            # wybieram losowe inty z przedziału 1, n
            sa_i = randint(1, sa_n)
            sa_j = randint(1, sa_n)
            sa_pi_new = sa_pi[:]
            # wykonuje losowy ruch: swap
            sa_pi_new = swap(sa_pi_new, sa_i - 1, sa_j - 1)

            sa_pi_C = Calc_Cmax(sa_p, sa_pi, sa_M)
            sa_pi_new_C = Calc_Cmax(sa_p, sa_pi_new, sa_M)

            # sprawdzamy czy po wykonaniu swap Cmax się zwiekszyl:
            #
            # jezeli tak to pi jest podstawiane zależnie od prawdopodobienstwa
            if sa_pi_new_C[sa_n-1][sa_m-1] > sa_pi_C[sa_n-1][sa_m-1]:
                # wybranie losowej wartości r
                sa_r = random()
                # obliczenie prawdopodobienstwa zamiany
                sa_prob = Calc_prob(sa_pi_C[sa_n-1][sa_m-1], sa_pi_new_C[sa_n-1][sa_m-1], sa_T)
                # jeżeli r jest większe, równe prawdopodobienstwu podstawiamy pi_new do pi
                if sa_r >= sa_prob:
                    sa_pi_new = sa_pi[:]
    
            sa_pi = sa_pi_new[:]

            sa_final_pi_C = Calc_Cmax(sa_p, sa_final_pi, sa_M)
            # jezeli Cmax zmalal po prostu podstawiamy
            if sa_pi_C[sa_n-1][sa_m-1] < sa_final_pi_C[sa_n-1][sa_m-1]:
                sa_final_pi = sa_pi[:]
        # Obnizamy temperature
        sa_T = ReduceTemperature(sa_T, sa_L)
    return sa_final_pi


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

    disp_all(n, m, p, N, M)

    main_sa_pi = []
    main_T0 = 500
    main_Tend = 25
    main_it = 50

    start_time = time.time()
    main_sa_pi = simuAnnealing(n, m, p, N, M, main_T0, main_Tend, main_it)
    tmp_time = time.time() - start_time
    main_sa_pi_C = Calc_Cmax(p, main_sa_pi, M)

    print("Sim.Annealing pi: ", end='')
    print(main_sa_pi, end='')
    print("       Cmax: ", end='')
    print(main_sa_pi_C[n-1][m-1], end='')
    print("       Czas działania: %.5s s" % tmp_time, end='')
    print("       il. iteracji ", main_it)


main()