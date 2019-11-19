"""Escribir un programa que lea una frase, y pase ésta como parámetro a una función
que debe contar el número de palabras que contiene.
Debe imprimir el programa principal el resultado.
Asumir que cada palabra está separada por un solo blanco:"""
"""A) Asumir que cada palabra está separada por un solo blanco."""
"""B) No se sabe cómo están separadas las palabras.
Pueden estar separadas por más de un blanco o por signos de puntuación."""
#Francisco Llamas
#A
def f(frase, espacio):
    for i in frase:
        if i==" ":
            espacio=espacio+1
    print("El numero de palabras es", espacio)
            
#prog principal
frase=input("introduzca una frase")
espacio=1
f(frase, espacio)



