"""Escribe un programa que te pida una frase, y pase la frase
como parámetro a una función. Ésta debe devolver si es palíndroma o no
, y el programa principal escribirá el resultado por pantalla:"""
#Francisco Llamas
def f(frase, palindromo):
    print(frase)
    if palindromo==frase.replace(" ",""):
        print("su frase es", frase,"es un palindromo")
    else:
        print("su frase",frase,"no es un palindromo")

#prog principal
frase=input("introduzca su frase")
palindromo=frase.replace(" ","")[::-1]
f(frase, palindromo)
frase.replace(" ","")
