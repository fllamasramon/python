palabras=["uno","dos","tres"]
diccionario=[]
palabra2=["cuatro","cinco","seis"]
diccionario.append(palabras)
diccionario.append(palabra2)
for i in range(len(diccionario)):
    for j in range(len(diccionario[i])):
        print(diccionario[i][j])
