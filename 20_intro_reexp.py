import re

# son patrones utilizados para encontrar una determinada combinacion
# de caracteres dentro de una cadena de texto

Texto = '''Juan Diego Gomez 3213213 rojo azul verde juan@mail.com
Juan Camilo Perez 4341234 azul azul verde camino@mail.com
Ana Maria Avila 233123123 verde verde verde ana@mail.com'''

# nos dice donde encontro la palabra por primera vez
print(re.search('azul', Texto)) # azul está en el texto
print(re.search('morado', Texto)) # morado no está en el texto

if re.search('azul', Texto):
    print('palabra encontrada')
else:
    print('palabra no encontrada')

# busca todas las veces que aparece esta palabra 
print(re.findall('azul', Texto))

print(re.findall('Juan', Texto, re.I)) # ignora las mayus

# estudios de los limites
print(re.findall('^Juan', Texto, re.M)) # busca en cada linea: re.M
print(re.findall('.com$', Texto, re.M)) # busca en cada linea: re.M
print(re.findall(r'\b3\B', Texto))
