
import numpy as np
import re

string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1 ,4, 4)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

txt = '(734) 647-6333'
result1 = re.search(r'[(]\d{3}[)]\s\d{3}[-]\d{4}', txt)
print(result1)

import pandas as pd
serie1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
serie2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})
serie2.loc[1]