import numpy as np
import random
import time

W = {"A": 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}


def uz(droga, a, b, wa):
    droga[W[a]][W[b]] = wa
    droga[W[b]][W[a]] = wa
    return droga


Drogi = [    [ 0, -1, -1, -1, -1, -1, -1],  #A
             [-1,  0, -1, -1, -1, -1, -1],  #B
             [-1, -1,  0, -1, -1, -1, -1],  #C
             [-1, -1, -1,  0, -1, -1, -1],  #D
             [-1, -1, -1, -1,  0, -1, -1],  #E
             [-1, -1, -1, -1, -1,  0, -1],  #F
             [-1, -1, -1, -1, -1, -1,  0]   #G
]

Drogi = uz(Drogi, 'A', 'C', 1)
Drogi = uz(Drogi, 'A', 'D', 2)
Drogi = uz(Drogi, 'C', 'B', 2)
Drogi = uz(Drogi, 'C', 'D', 1)
Drogi = uz(Drogi, 'C', 'E', 3)
Drogi = uz(Drogi, 'F', 'E', 2)
Drogi = uz(Drogi, 'B', 'F', 3)
Drogi = uz(Drogi, 'D', 'G', 1)
Drogi = uz(Drogi, 'G', 'F', 1)
Indeksy = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def oblicz(p, k):

    print("  0    1    2    3    4    5    6")
    print(Indeksy)
    print("\n")

    S = []                                                                          # WIERZCHOLKI PRZETWORZONE
    Q = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}                                         # WIERZCHOLKI DO PRZETWORZENIA
    D_W = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -1, 'G': -1}           # Koszty drog
    Poprzednicy = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -1, 'G': -1}   # Poprzednicy wezlow

    Q.discard(p)
    D_W[p] = 0
    S.append(p)
    najmniejszy_w = p

    for i in Indeksy:
        if Drogi[W[najmniejszy_w]][W[i]] > 0:
            if D_W[i] > Drogi[W[najmniejszy_w]][W[i]] or D_W[i] < 0:
                D_W[i] = Drogi[W[najmniejszy_w]][W[i]]
                Poprzednicy[i] = W[najmniejszy_w]

    while len(Q) > 0:

        wartosc = 100

        for i in Q:                                          # Dla wszystkich otaczajacych wierzcholkow
            if Drogi[W[najmniejszy_w]][W[i]] > 0:            # Sprawdz czy jest do nich polaczenie
                    if D_W[i] > Drogi[W[najmniejszy_w]][W[i]] + D_W[najmniejszy_w] or D_W[i] < 0:
                        D_W[i] = Drogi[W[najmniejszy_w]][W[i]] + D_W[najmniejszy_w]
                        Poprzednicy[i] = W[najmniejszy_w]

        # Wybieram najmniejsze drogi
        for i in Q:
            if 0 < D_W[i] < wartosc:
                najmniejszy_w = i
                wartosc = D_W[i]

        S.append(najmniejszy_w)                        # dodaj wyszukany wierzcholek do nastepnego kroku
        Q.discard(najmniejszy_w)                       # Usun wierzcholek ze swojej listy wiercholkow

    return D_W, S, Poprzednicy

Start = 'E'
Koniec = 'D'
Droga, s4, s5 = oblicz(Start, Koniec)

zm = s5[Koniec]
Najkrotsza_sciezka=[]
Najkrotsza_sciezka.append(Koniec)

while zm > 0:
    Najkrotsza_sciezka.append(Indeksy[zm])
    zm = s5[Indeksy[zm]]



print("Najkrotsza sciezka")
print(Najkrotsza_sciezka)
print("Poprzednie")
print(s5)

print("Wartosci drog:")
print(Droga)

print("Zbior przetworzonych:")
print(s4)
