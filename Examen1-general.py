'''
Listas y Bucles:
a) Dada una lista de números, calcula la suma de todos los elementos.
b) Dada una lista de palabras, crea una nueva lista que contenga la longitud de cada palabra.

Tuplas y Operaciones:
a) Crea una tupla con números enteros de tu elección y calcula su suma y su producto.
b) Crea dos tuplas y combínalas para formar una nueva tupla.

Diccionarios y Bucles:
a) Crea un diccionario con nombres de países como claves y sus capitales como valores.
b) Dada una lista de números, crea un diccionario donde las claves sean los números y los valores sean sus cuadrados.

Sets y Operaciones:
a) Dada una lista de números duplicados, crea un set que contenga solo los valores únicos.
b) Crea dos sets y encuentra la intersección y la unión de ambos.

Funciones:
a) Escribe una función que tome una lista de números y devuelva el promedio de los elementos.
b) Escribe una función que tome una cadena y devuelva la cadena invertida.

Condicionales:
a) Escribe un programa que tome un número y determine si es par o impar.
b) Escribe un programa que tome una edad y determine si es un niño (menor de 12 años), adolescente (entre 12 y 18 años) o adulto.

Loops y Control de Flujo:
a) Escribe un programa que muestre los números del 1 al 10 utilizando un bucle while.
b) Escribe un programa que imprima los números pares del 1 al 20 utilizando un bucle for.

Archivos:
a) Crea un archivo de texto y escribe algunas líneas en él.
b) Lee el contenido del archivo que creaste y muestra su contenido por pantalla.

'''

'''
Listas y Bucles:
a) Dada una lista de números, calcula la suma de todos los elementos.
b) Dada una lista de palabras, crea una nueva lista que contenga la longitud de cada palabra.

lista=[1,2,3,4,5]
print(len(lista))
suma=0
for i in lista:
    suma+=i
print(suma)
#falta con lambda 

palabras=['amor', 'felicidad', 'tranquilidad']
new_words=[len(j) for j in palabras]
print(new_words)

'''

#empezando 

'''
Tuplas y Operaciones:
a) Crea una tupla con números enteros de tu elección y calcula su suma y su producto.
b) Crea dos tuplas y combínalas para formar una nueva tupla.

tuplas_1=(2,3,6,9)
tuplas_2=(5,8,6,3,7,12)
suma=0

for i in tuplas_1:
    suma+=i
print(f'la suma es igual a {suma}')

new=(tuple(zip(tuplas_1,tuplas_2)))
print(new)

'''

'''
Diccionarios y Bucles:
a) Crea un diccionario con nombres de países como claves y sus capitales como valores.
b) Dada una lista de números, crea un diccionario donde las claves sean los números y los valores sean sus cuadrados.7

#Empezando. 
paises={
    'Colombia': 'Bogotá',
    'Francia':'Paris', 
    'Usa': 'Washinton'
}
print(paises)

numeros=[1,2,3,4,5,6]
diccionario={k:k*2 for k in numeros}
print(diccionario)
'''



'''
Sets y Operaciones:
a) Dada una lista de números duplicados, crea un set que contenga solo los valores únicos.
b) Crea dos sets y encuentra la intersección y la unión de ambos.

sets=[1,6,5,3,3,1,2,8,3,5]
print(set(sets))

set_1={1,6,32,56,3,1,5,9,5}
set_2={9,2,1,78,54,3,5,21}

print(set_1|set_2)
print(set_1 & set_2)

'''



'''
Condicionales:
a) Escribe un programa que tome un número y determine si es par o impar.
b) Escribe un programa que tome una edad y determine si es un niño (menor de 12 años), adolescente (entre 12 y 18 años) o adulto.

num=int(input(' digite el numero: '))
if num %2==0 :
    print('par')
else:
    print('impar')

edad=10
if edad < 12:
    print('niño')
elif 12<edad>18:
    print('adolecente')
else:
    print('adulto')

'''

'''
Loops y Control de Flujo:
a) Escribe un programa que muestre los números del 1 al 10 utilizando un bucle while.
b) Escribe un programa que imprima los números pares del 1 al 20 utilizando un bucle for.

'''
for i in range (0,21,2):
    print(i)

num=1
while num<11:
    print(num)
    num+=1
    



















