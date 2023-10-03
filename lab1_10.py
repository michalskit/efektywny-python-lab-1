import timeit

# Uzupełnij poniższe impementacje tak aby czas wykonania
# is_perfect2 << is_perfect1

# Podejście 1
def is_perfect(n):
    '''W tym podejściu, dla każdej liczby n, znajdujemy
    wszystkie jej dzielniki i sumujemy je. Następnie
    porównujemy sumę z n. Jeśli są równe, liczba jest
    doskonała.'''
    pass


# Podejście 2
def is_perfect2(n):
    '''W tym podejściu proszę zastosować zoptymalizowany
    algorytmy, które skupiają się na poszukiwaniu liczb
    doskonałych.'''
    pass


# Mierzenie czasu wykonania
def time_is_perfect():
  for i in range(1, 1000):
    is_perfect(i)


def time_is_perfect2():
  for i in range(1, 1000):
    is_perfect2(i)


czas_is_perfect = timeit.timeit(time_is_perfect, number=40)
czas_is_perfect2 = timeit.timeit(time_is_perfect2, number=40)

print(f'Czas wykonania is_perfect: {czas_is_perfect:.2f} sekundy')
print(f'Czas wykonania is_perfect2: {czas_is_perfect2:.2f} sekundy')