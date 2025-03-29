doc = open('regex.txt', 'r')
texto = doc.read()
doc.close()

# print(texto)

import re
Aureliano = re.findall(r'Aureliano', texto, re.I)
print(len(Aureliano))


