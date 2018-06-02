import itertools
import numpy as np
import sys

klucz = int(input("Podaj wielkość klucza: "))
fence_iterators = [] # lista do iterowania

for x in range(0, klucz - 1):  # przygotowujemy liste do iterowania
    fence_iterators.append(x)  
for y in range(klucz -1, 0, -1):
    fence_iterators.append(y)

print(fence_iterators)


m_iter = max(fence_iterators) + 1

def szyfruj():
    plain_text = str(input("Podaj wiadomość: ")) # tekst do zaszyfrowania
    string_len = len(plain_text) # dlugosc tekstu

    fence = np.empty((m_iter, string_len), dtype = str) # tablica 2-wymiarowa, w ktora wpisujemy tekst do zaszyfrowania

    for c, i, v in zip(plain_text, itertools.cycle(fence_iterators), range(0, string_len)):  # wpisywanie znakow do macierzy
        fence[i, v] = c
    print(fence)

    kryptogram = ''   # zmienna przechowujaca tekst w zaszyfrowanej formie
    for v in range(m_iter): # zczytujemy tekst z macierzy od lewej do prawej, wiersz po wierszu
        for c in range(string_len):
            kryptogram += fence[v, c]

    print("Kryptogram:", kryptogram)
    return kryptogram



def deszyfruj():
    cripto = input("Podaj szyfr: ") # zmienna przechowujaca tekst w zaszyfrowanej formie
    string_len = len(cripto) # sprawdzamy z ilu znakow sklada sie tekst

    fence = np.empty((m_iter, string_len), dtype = str) # przygotowujemy macierz do wpisania kryptogramu
    for i, v in zip(itertools.cycle(fence_iterators), range(0, string_len)): # oznaczamy miejsca, w ktorych maja znalezc sie znaki gwiazdką *
        fence[i, v] = '*'

    i = 0  # zmienna przechowujaca numer indeksu w zmiennej kryptogram
    decripted = '' # zmienna przechowujaca odszyfrowany tekst
    for v in range(m_iter):
        for c in range(string_len):
            if fence[v, c] == '*':      
                fence[v, c] = cripto[i] # jeśli napotkamy znak *, zastępujemy go kolejną literą kryptogramu
                i += 1


    for i, v in zip(itertools.cycle(fence_iterators), range(0, string_len)): # zczytujemy znaki z tablicy w kolejności zgodnej z szyfrowaniem płotkowym
        decripted += fence[i, v]
    print("Wiadomość: " + decripted)



############# PROGRAM #############

while 1:
    print("Zaszyfruj - 1 \nOdszyfruj - 2 \nZakończ - 0")
    try:
        opcja = int(input("Opcja: "))
        if opcja == 1:
              szyfruj()
        if opcja == 2:
            deszyfruj()
        if opcja == 0:
            sys.exit(1)
    except ValueError:
        print("\nNiepoprawna opcja. Spróbuj ponowanie\n")
        pass