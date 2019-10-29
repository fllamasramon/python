anchura=int(input("introduzca la anchrua"))
altura=int(input("escribe altura"))

print(anchura * "*")
for i in range(altura-2):
    print("*",(" "*(anchura-4)),"*")
print(anchura * "*")
