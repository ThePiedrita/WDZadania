import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1

#data=pd.read_excel('imiona (1).xlsx')
#df=pd.DataFrame(data)
#grupa=df.groupby('Rok').agg({'Liczba':['sum']})
#grupa.plot(xlabel='Lata',ylabel='Ilość',legend=False)


#Zadania 2

data=pd.read_excel('imiona (1).xlsx')
df=pd.DataFrame(data)
grupa=df.groupby('Plec').agg({'Liczba':['sum']})
grupa.plot(kind='bar',xlabel='Plec',ylabel='Ilość',legend=False,title='Suma Płci',rot=0)
plt.show()
