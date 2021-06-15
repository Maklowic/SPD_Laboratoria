#
# SYMULOWANE WYŻARZANIE
#
from RandomNumberGenerator import RandomNumberGenerator
import math
import time
from cw6_inne import *

#
# SYMULOWANE WYŻARZANIE
# 


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

    print("\n           Key to continue . . .")
    input()


main()
