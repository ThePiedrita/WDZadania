import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
daty = pd.date_range('20210324', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)
zam=pd.read_csv('zamowienia.csv',header=0, sep=';',decimal=',')
print(zam)

print("\nZADANIE 1")
narodziny=pd.read_excel('imiona.xlsx',header=0)
df=pd.DataFrame(narodziny)
print(df)