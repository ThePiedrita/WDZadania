import numpy as np

print('ZADANIE 1')
tab=np.arange(4,84,4)
print(tab)

print('\nZADANIE 2')
a=np.arange(1,5,0.5)
b=a.astype(dtype='int32')
print(a.dtype)
print(b.dtype)

print('\nZADANIE 3')
def tablica(n):
    t=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            t[i][j]=2**(i+j)
    return t
print(tablica(5))

print('\nZADANIE 4')
def potegi(pod,ilosc):
    potegi = np.logspace(0, ilosc - 1, num=ilosc, base=pod)
    return potegi
print(potegi(2,4))

print('\nZADANIE 5')
def macierz(n):
    reversed_vector = np.arange(n)[::-1]
    diagonal_vector = np.diag(reversed_vector, k=2)
    return diagonal_vector
print(macierz(5))

print('\nZADANIE 6')
words=['kon','kot','kac']
matrix=np.zeros((3,3),dtype='U1')

for i, word in enumerate(words):
    matrix[i, :len(word)] = list(word)

print('\nZADANIE 7')
def genmacierz(n):

    matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        matrix[i, i] = 2 * (i + 1)
        if i < n - 1:
            matrix[i, i + 1] = 2 * (i + 1)
            matrix[i + 1, i] = 2 * (i + 1)

    return matrix

print('\nZADANIE 8')
def array(arr, direction):
    if direction == 'vertical':
        if arr.shape[0] % 2 != 0:
            print('Ilość wierszy nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[0] // 2
            return arr[:half], arr[half:]
    elif direction == 'horizontal':
        if arr.shape[1] % 2 != 0:
            print('Ilość kolumn nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[1] // 2
            return arr[:, :half], arr[:, half:]
    else:
        print('Nieprawidłowy kierunek podziału.')
        return arr
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)

    # Podział pionowy
    arr1, arr2 = divide_array(arr, 'vertical')
    print(arr1)
    print(arr2)

    # Podział poziomy
    arr3, arr4 = divide_array(arr, 'horizontal')
    print(arr3)
    print(arr4)

    # Nieprawidłowy kierunek podziału
    arr5 = divide_array(arr, 'wrong')
    print(arr5)

    print('\nZADANIE 9')

    # wygenerowanie tablicy jednowymiarowej
    arr = np.arange(1, 26)

    # zmiana kształtu na macierz 5x5
    arr = arr.reshape((5, 5))

    print(arr)