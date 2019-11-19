"""Escribe un programa que pida dos palabras las pase como parámetro
a un procedimiento y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un poco
y si no, que no riman."""
#Francisco Llamas
def f(palabra1, palabra2):
    if palabra1[-3:]==palabra2[-3:]:
        print("tus palabras riman")
    elif palabra1[-2:]==palabra2[-2:]:
        print("tus palabras riman un poco")
    else:
        print("tus palabras no riman")
    
#prog principal
palabra1=input("escriba una palabra")
palabra2=input("escriba otra palabra")
f(palabra1, palabra2)

