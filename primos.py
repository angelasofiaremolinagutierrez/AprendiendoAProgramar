from __future__ import print_function
import sys

#pedir numero
numero = int(sys.argv[1])

#hallar la raiz
raiz = int(numero**0.5)

#lista numeros desde 2 hasta la raiz
lista = range(2,raiz+1)

contador=0

#num es un elemento de la lista
#hacer numero % elementolista
for num in lista:
	modulo = numero % num
	if(modulo==0):
		contador = contador +1 

#contar ceros
if(contador == 0):
	print("El numero es primo")

else:
	print("El numero no es primo")

