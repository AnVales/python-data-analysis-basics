import re

# son patrones utilizados para encontrar una determinada combinacion
# de caracteres dentro de una cadena de texto

Texto1 = '''Juan Diego Gomez 3213213 rojo azul verde juan@mail.com
Juan Camilo Perez 4341234 azul azul verde camino@mail.com
Ana Maria Avila 233123123 verde verde verde ana@mail.com'''

Texto2 = ''' Beto M1235 M
Ana U1246 S
Jaime M432 S
Maria U324 M'''

Texto3 = '''ruta12: http://pagina.com
ruta15: https://ejemplo.com
ruta22: http://www.pagina.com
ruta28: https://www.ejemplo.com'''

print(re.findall(r'\w+', Texto2))
print(re.findall(r'M\d+', Texto2))
print(re.findall(r'M\d{4}', Texto2))

print(re.findall(r'\w+@mail.com', Texto1))

print(re.findall(r'ruta[2-9]+', Texto3))

# buscar paginas y unirlas en una lista
paginas = re.findall(r'(https://|http://)(w{3}.?)?(\w+.com)', Texto3)
paginas = [''.join(pagina) for pagina in paginas]
print(paginas)
