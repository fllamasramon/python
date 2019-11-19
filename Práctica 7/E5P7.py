"""Escribe un programa que te pida una frase y una vocal,
y pase estos datos como parámetro a una función
que se encargará de cambiar todas las vocales de la frase
por la vocal seleccionada. Devolverá la función la frase modificada,
y el programa principal la imprimirá:"""
#Francisco Llamas
def f(frase, vocal):
    for i in frase:
        if i in vocales:
            print(vocal, end="")
        else:
            print(i, end="")

#prog principal
frase=input("escriba una frase")
vocal=input("escriba una vocal")
vocales=["a","e","i","o","u"]
f(frase, vocal)
