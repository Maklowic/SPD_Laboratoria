from RandomNumberGenerator import RandomNumberGenerator
from Task import Task
from Foo import *


def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj rozmiar problemu: "))
    # dwie opcje indeksowania:
    # problems = range(1, n + 1) #[1, 2, 3, 4, 5, 6] <-- realne indeksy liczone od 1

    # ponizsza wersja: [0, 1, 2, 3, 4, 5]     <-- komputerowe indeksy liczone od 0
    problems = range(0, n)

    rng = RandomNumberGenerator(seed)

    J = []  # tu beda przechowywane obiekty klasy Task
    # jako j beda oznaczane numery elementow ze zbioru J (nie indeksy tabeli)

    # Generowanie obiektów
    for i in problems:
        newTask = Task()  # tworzy nowy obiekt
        J.append(newTask)  # dodaje go do listy obiektow

    N = []  # tutaj będą wpisane numery zadan ze zbioru J.

    # Generowanie czasu p
    for j in problems:
        # dla kazdego zadania j ze zbioru J generuje wartosc p_j
        J[j].p = rng.nextInt(1, 29)

        # W obu miejscach ponizej wpisujemy numery zadan np [1, 2, 3, 4, 5, 6]
        J[j].number = j+1
        N.append(j+1)

    G = []  # zbior zadan gotowych jest pusty
    A = set_A(J)  # funkcja oblicza sume czasow p zadan ze zbioru J
    X = A

    # Generowanie czasu r
    for j in problems:
        # dla kazdego zadania j ze zbioru J generuje wartosc r_j
        J[j].r = rng.nextInt(1, A)

    # Generowanie czasu q
    for i in problems:
        # dla kazdego zadania j ze zbioru J generuje wartosc q_j
        J[i].q = rng.nextInt(1, X)

    print("\nStan poczatkowy:")
    # funkcja wyswietla w trzech wierszach warto r, p, q kolejnych zadan, np.
    Print_all(J)
    # r: [ 4 44 44 60 25 34 ]
    # p: [ 1 4 22 14 16 7 ]
    # q: [ 54 3 4 34 43 1 ]

    print("")  # enter odstepu dla czytelnosci (python automatycznie daje enter, wiec \n oznaczaloby dwa entery)

    # przed petla while potrzebujemy miec juz ustalona wartosc t
    t = min_r(J, N)
    pi = []  # tutaj bedzie zapisywana kolejnosc zadan

    while N or G:  # petla dziala dopoki oba zbiory nie sa puste, czyli dopoki sa zadania do przerobienia
        while N and min_r(J, N) <= t:
            # przypomnienie: j to nie indeksy listy, tylko numery zadan 1, 2, 3...
            # wybiera zadanie z niegotowych zadan o najmniejsyzm czasie r
            j = arg_min_r(J, N)
            G.append(j)  # dodaje numer zadania do zbioru gotowych zadan
            N.remove(j)  # usuwa numer zadania ze zbioru niegotowych
            # tab.remove(i) usuwa element z tablicy tab o wartosci i

        if G:
            # wybiera zadanie z gotowych zadan o najwiekszym czasie q
            j = arg_max_q(J, G)
            G.remove(j)  # usuwa wykonane zadanie z gotowych zadan
            # wstawia numer zadania do permutacji (kolejnosci zadan)
            pi.append(j)
            t = t + J[j-1].p  # ustala chwile wykonania zadania (bez czasu q)
            # przypisuje zadaniu czas zakonczenia (wraz z czasem q)
            J[j-1].C = t + J[j-1].q
        else:
            t = min_r(J, N)

    # Wyswietla permutacje pi
    print("pi: ", end='')
    print(pi)

    # Wyswietla wszystkie lokalne czasy C zadan oraz Cmax
    Print_C(J)


main()
