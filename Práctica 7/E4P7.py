"""Escribe un programa que pida una frase, y le pase como parámetro
a una función dicha frase. La función debe sustituir todos los espacios
en blanco de una frase por un asterisco,
y devolver el resultado para que el programa
principal la imprima por pantalla."""
#Francisco Llamas
def f(frase):
    for i in frase:
        if i==" ":
            print("*")
        else:
            print(i)

#prog principal
frase=input("escriba una frase")
f(frase)
