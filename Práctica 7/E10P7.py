"""Escribe un programa que te pida una palabra o número,
pase por parámetro estos datos a una función,
y ésta te diga si es o no palíndroma o capicúa.
El programa principal imprimirá el resultado de la función:"""
#Francisco Llamas
def f(numero, palindromo):
    if palindromo==numero:
        return print("Es capicua y/o palindromo")
    else:
        return print("no es capicua ni palindromo")

#prog principal
numero=input("introduzca el numero o la palabra")
palindromo=numero[::-1]
f(numero, palindromo)

#for i in range(0, len(numero), -1) = [::-1]
