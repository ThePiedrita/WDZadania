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
    t=np.logspace(pod,1,num=ilosc)
    return t
print(potegi(2,4))