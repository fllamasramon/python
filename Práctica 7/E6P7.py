"""Escribe un programa que lea el nombre de una persona y un carácter,
le pase estos datos a una función que comprobará si dicho carácter está
en su nombre. El resultado de dicha función lo imprimirá el programa principal
por pantalla."""
#Francisco Llamas
def f(nombre, caracter):
    for i in nombre:
        if i==caracter:
            return print("tu caracter", caracter, "esta en tu nombre", nombre)
    print("el caracter no esta")

#prog principal
nombre=input("escribe tu nombre")
caracter=input("escribre tu caracter")
f(nombre, caracter)


