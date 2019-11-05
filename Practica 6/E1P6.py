"""Escribe un programa que te pida palabras y las guarde en una lista.
Para terminar de introducir palabras, simplemente pulsa Enter.
El programa termina escribiendo la lista de palabras."""
#Francisco Llamas
palabras=[]
entrada=input("dame una palabra")

while entrada!="":
    palabras.append(entrada)
    entrada=input("dame una palabra")

print("las palabras introducidas son: ", palabras)
