from RandomNumberGenerator import RandomNumberGenerator
import math
import time
from random import randint
from random import random
from cw6_inne import *

#
# PRZESUKIWANIE Z ZABRONIENIAMI
#

def tabuSearch(liczba_zadan, liczba_maszyn, tablica_p, tablica_N, tablica_M):
    tabu_n = liczba_zadan
    tabu_m = liczba_maszyn
    tabu_p = tablica_p[:]
    tabu_N = tablica_N[:]
    tabu_M = tablica_M[:]
    tabu_pi = []
    tabu_final_pi = []
    tabu_list = []

    # dobrane testowo
    czas_kadencji = tabu_n

    # wstepne naszykowanie permutacji jako permutacja naturalna
    for problem in range(1, tabu_n+1):
        tabu_pi.append(problem)

        # ta tablica sluzy w ostatnie czesci funkcji do porownywania permutacji
        tabu_final_pi.append(problem)

    # stworzenie listy tabu w postaci macierzy
    for j in range(0, tabu_n):
        tmp = []
        for i in range(0, tabu_n):
            tmp.append(0)
        tabu_list.append(tmp)

    # mnożnik dobrany testowo, konwersja do int w przypadku zastosowania zmiennych typu float
    limit_iteracji = int(5 * czas_kadencji)

    # tyle iteracji, ile narzuca limit_iteracji
    for iteracja in range(1, limit_iteracji+1):
        Cbest = 99999

        # for j = 1 to n do
        for j in range(1, tabu_n):

            # for k = j + 1 to n do
            for k in range(j+1, tabu_n+1):

                # sprawdzamy, czy kadencja sie skonczyla
                if tabu_list[j-1][k-1] < iteracja:

                    # jezeli kadencja sie skonczyla, to na kopii sprawdzamy, czy uzyskamy w ten sposob lepszy wynik
                    tabu_pi_kopia = tabu_pi[:]

                    # zamieniamy wartosci miejscami
                    tabu_pi_kopia[j-1], tabu_pi_kopia[k -
                                                      1] = tabu_pi_kopia[k-1], tabu_pi_kopia[j-1]

                    # liczymy wartosc Cbest nowego rozwiazania
                    tabu_C = Calc_Cmax(tabu_p, tabu_pi, tabu_M)
                    # print(tabu_C)

                    # porownujemy nowy wynik z poprzednim
                    if tabu_C[tabu_n-1][tabu_m-1] < Cbest:
                        Cbest = tabu_C[tabu_n-1][tabu_m-1]
                        nowe_j = j
                        nowe_k = k

        # zamieniamy dwie wartosci permutacji na podstawie wybranych indeksow
        tabu_pi[nowe_j-1], tabu_pi[nowe_k -
                                   1] = tabu_pi[nowe_k-1], tabu_pi[nowe_j-1]

        # wprowadzamy nowa kadencje dla dwoch indeksow
        tabu_list[nowe_j-1][nowe_k-1] = iteracja + czas_kadencji

        # liczymy wartosc Cbest nowego rozwiazania i starego
        tabu_pi_C = Calc_Cmax(tabu_p, tabu_pi, tabu_M)
        tabu_final_pi_C = Calc_Cmax(tabu_p, tabu_final_pi, tabu_M)

        # porownujemy nowy wynik z poprzednim
        if tabu_pi_C[tabu_n-1][tabu_m-1] < tabu_final_pi_C[tabu_n-1][tabu_m-1]:
            tabu_final_pi = tabu_pi[:]

    return tabu_final_pi

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

    main_tabu_pi = []
    start_time = time.time()
    main_tabu_pi = tabuSearch(n, m, p, N, M)
    tmp_time = time.time() - start_time
    main_tabu_pi_C = Calc_Cmax(p, main_tabu_pi, M)

    print("Tabu          pi: ", end='')
    print(main_tabu_pi, end='')
    print("       Cmax: ", end='')
    print(main_tabu_pi_C[n-1][m-1], end='')
    print("       Czas działania: %.5s s" % tmp_time)


main()