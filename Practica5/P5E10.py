filas=int(input("introduce la altura del triangulo"))
for i in range(filas):
    print(" "*(filas-i-1)+"*"*(2*i+1))
