"""Escribe un programa que pida una frase, y pase la frase como parámetro
a una función que debe eliminar los espacios en blanco (compactar la frase).
El programa principal imprimirá por pantalla el resultado final."""
#Francisco Llamas
def f(frase):
    for i in frase:
        if i==" ":
            print("", end="")
        else:
            print(i, end="")
    return True

#prog principal
frase=input("escriba su frase")
f(frase)
