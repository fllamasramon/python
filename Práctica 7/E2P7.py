"""Escribe un programa que lea el nombre y los dos apellidos de una persona
(en tres cadenas de caracteres diferentes),
los pase como parámetros a una función,
y ésta debe unirlosy devolver una única cadena.
La cadena final la imprimirá el programapor pantalla."""
#Francisco Llamas
def f():
    nombre=input("introduzca su nombre")
    PrimerApellido=input("introduzca su primer apellido")
    SegundoApellido=input("introduzca su segundo apellido")
    return nombre, PrimerApellido, SegundoApellido

#prog principal
lista=f()
print(lista)
