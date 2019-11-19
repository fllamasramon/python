"""Escribe un programa que lea una frase, y la pase como parámetro
a un procedimiento. El procedimiento contará el número de vocales (de cada una)
que aparecen, y lo imprimirá por pantalla."""
#Francisco Llamas
def f(frase, vocalesa, vocalese, vocalesi, vocaleso, vocalesu):
    for i in frase:
        if i.lower()=="a":
            vocalesa+=1
        if i.lower()=="e":
            vocalese+=1
        if i.lower()=="i":
            vocalesi+=1
        if i.lower()=="o":
            vocaleso+=1
        if i.lower()=="u":
            vocalesu+=1

    print("La cantidad de A es", vocalesa, "La cantidad de E es", vocalese,
          "La cantidad de I es",  vocalesi, "La cantidad de O es", vocaleso,
          "La cantidad de U es", vocalesu,)

#prog principal
frase=input("escriba su frase")
vocalesa=0
vocalese=0
vocalesi=0
vocaleso=0
vocalesu=0
f(frase, vocalesa, vocalese, vocalesi, vocaleso, vocalesu)



