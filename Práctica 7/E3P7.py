"""Escribe un programa que lea una frase, y la pase como parámetro
a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea."""
#Francisco Llamas
def f(frase):
    for i in frase:
        print(i)

#prog principal
frase=input("escriba una frase")
f(frase)
    

    
