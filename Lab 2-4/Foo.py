'''
Taka zaleznosc:
tablica: tab = [10, 20, 30, 40, 50, 60]

Opcja 1:
for i in range(0, len(tab)):
    print(i)

wtedy wyswietli 0 1 2 3 4 5, bo range (zasieg) od 0 do 6 (czyli w pythonie realnie zasieg 0-5)

Natomiast opcja 2:
for i in tab:
    print(i)

wyswietli 10 20 30 40 50 60, bo wyswietla element "i" ze zbioru tab
'''


def Print_J(tab):
    print("[ ", end='')
    for i in tab:
        print(i.number, end=' ')
    print("]")


def Print_r(tab):
    print("[ ", end='')
    for i in tab:
        print(i.r, end=' ')
    print("]")


def Print_p(tab):
    print("[ ", end='')
    for i in tab:
        print(i.p, end=' ')
    print("]")


def Print_q(tab):
    print("[ ", end='')
    for i in tab:
        print(i.q, end=' ')
    print("]")


def Print_C(tab):
    Cmax = -1
    print("C: [ ", end='')
    for i in tab:
        print(i.C, end=' ')
        Cmax = max(Cmax, i.C)
    print("]")
    print("Cmax: ", end='')
    print(Cmax)


def Print_all(tab):
    print("J: ", end='')
    Print_J(tab)
    print("r: ", end='')
    Print_r(tab)
    print("p: ", end='')
    Print_p(tab)
    print("q: ", end='')
    Print_q(tab)


def set_A(tab):
    sum = 0
    for i in tab:
        sum = sum + i.p  # pobiera wartosc p z kolejnych zadan i ze zbioru tab
    return sum


def min_r(J, N):
    min_r = 10000
    for i in N:  # i jest jedna z wartosci ze zbioru tab
        if min_r > J[i-1].r:
            min_r = J[i-1].r
    return min_r

def q_min_r(J, N):
    min_r = 10000
    for i in N.queue:  # i jest jedna z wartosci ze zbioru tab
        if min_r > i.r:
            min_r = i.r
    return min_r

def arg_min_r(J, N):
    min_r = 10000
    for i in N:  # tutaj i jest indeksem, a nie wartoscia z tabeli tab
        if min_r > J[i-1].r:
            min_r = J[i-1].r
            id = i
    return id


def arg_max_q(J, G):
    max_q = -1
    for i in G:  # tutaj i jest indeksem, a nie wartoscia z tabeli tab
        if max_q < J[i-1].q:
            max_q = J[i-1].q
            id = i
    return id
