altura=int(input("por favor introduza la altura del rectángulo"))
ancho=int(input("por favor introduzca el ancho del rectángulo"))
for i in range(altura):
    for j in range(ancho):
        if (j==0 or j==ancho-1 or i==0 or i==altura-1):
            print("*", end="")
        else:
            print(" ",end="")
    print()
