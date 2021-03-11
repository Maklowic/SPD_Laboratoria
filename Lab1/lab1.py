from RandomNumberGenerator import RandomNumberGenerator


def main():
    seed = int(input("Podaj seed: "))
    n = int(input("Podaj rozmiar problemu: "))
    problems = range(1, n + 1)

    rng = RandomNumberGenerator(seed)
    nr = []
    p = []
    r = []

    # Generowanie czasu wykonywania p
    for problem in problems:
        nr.append(problem)
        p.append(rng.nextInt(1, 29))

    A = sum(p)

    # Generowanie czasu wykonywaniar
    for problem in problems:
        r.append(rng.nextInt(1, A))

    # Wyświetlenie tablic
    print("nr:", nr)
    print("r: ", r)
    print("p: ", p)

    # Ustalenie wartości wektora c
    C = []
    C.append(r[0]+p[0])
    for problem in range(1, n):
        C.append(max(C[problem-1], r[problem])+p[problem])

    # Ustalenie wartości wektora S
    S = [r[0]]
    for problem in range(1, n):
        S.append(max(r[problem], C[problem-1]))

    # Wyświetlenie wektorów S i c
    print("S: ", S)
    print("C: ", C)


main()
