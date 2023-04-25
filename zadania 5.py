import numpy as np
print('\nZADANIE 1')
macierz1=np.array([1,2,3])
macierz2=np.array([4,5,6])
wynik=np.dot(macierz1,macierz2)
print(wynik)

print('\nZADANIE 2')
macierz_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(macierz_a)
print("Najniższe wartości w każdym rzędzie macierzy 3x3:")
print(np.min(macierz_a, axis=1))
print("Najniższe wartości w każdej kolumnie macierzy 3x3:")
print(np.min(macierz_a, axis=0))

macierz_b = np.array([[4,2,6,7],[1,6,8,4],[5,6,4,9],[1,2,8,6]])
print(macierz_b)
print("Najniższe wartości w każdym rzędzie macierzy 4x4:")
print(np.min(macierz_b, axis=1))
print("Najniższe wartości w każdej kolumnie macierzy 4x4:")
print(np.min(macierz_b, axis=0))

print('\nZADANIE 3')
macierz2=macierz2.reshape(3,1)
wynik=np.dot(macierz1,macierz2)
print(wynik)

print('\nZADANIE 4')
macierz1 = np.array([1, 2, 3])
macierz2 = np.array([2.5, 3.5, 4.5])
iloczyn = np.dot(macierz1, macierz2)
print(iloczyn)

print('\nZADANIE 5')
macierz = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(macierz)
print(a)

print('\nZADANIE 6')
macierz = np.array([[0.5, 1, 1.5], [2, 2.5, 3]])
b = np.cos(macierz)
print(b)

print('\nZADANIE 7')
wynik_dodawania=a+b
print(wynik_dodawania)

print('\nZADANIE 8')
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
for row in mat:
    print(row)

print('\nZADANIE 9')
for elem in mat.flat:
    print(elem)

print('\nZADANIE 10')
mat = np.arange(81).reshape(9, 9)
print('Macierz 9x9:')
print(mat)
# zmiana kształtu macierzy na 3x27
mat_3x27 = mat.reshape(3, 27)
print('Macierz 3x27:')
print(mat_3x27)
# zmiana kształtu macierzy na 27x3
mat_27x3 = mat.reshape(27, 3)
print('Macierz 27x3:')
print(mat_27x3)
# zamiana kszrałtu macierzy na 81x1
mat_81x1 = mat.reshape(81, 1)
print('Macierz 81x1:')
print(mat_81x1)
# zamiana kszrałtu macierzy na 1x81
mat_1x81 = mat.reshape(1, 81)
print('Macierz 1x81:')
print(mat_1x81)

print('\nZADANIE 11')
vec = np.arange(12)
print(vec)

# przekształcenie wektora na macierz 3x4
mat_3x4 = vec.reshape((3, 4))
print('macierz 3x4')
print(mat_3x4)

# przekształcenie wektora na macierz 4x3
mat_4x3 = vec.reshape((4, 3))
print('macierz 4x3')
print(mat_4x3)

# przekształcenie wektora na macierz 2x6
mat_2x6 = vec.reshape((2, 6))
print('macierz 2x6')
print(mat_2x6)

# wyświetlenie spłaszczonych wersji macierzy
print(mat_3x4.flatten())
print(mat_4x3.flatten())
print(mat_2x6.flatten())

