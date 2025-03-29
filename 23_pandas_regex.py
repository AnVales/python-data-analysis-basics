import pandas as pd 
import re

dfreg = pd.DataFrame({
    'nombre': ['Pepito Gonzales', 'Maria Vasquez', 'Rosa Gomez', 'Pepito Chavez'],
    'codigo': ['co_123', 'pe_312', 'mx_546', 'mx_765'],
    'Abb': [11, 34, 12, 43],
    'Cdd': [12, 54, 67, 32]
})

dfreg = dfreg.set_index('codigo')
# print(dfreg)

dfreg1 = dfreg.filter(items= ['Abb', 'Cdd'])
# print(dfreg1)

dfreg2 = dfreg.filter(like= 'pe', axis = 0)
print(dfreg2)

dfre3 = dfreg.filter(regex= '\w{2}_[1-3]{3}', axis=0)
print(dfre3)