#Práctica 5 ejercicio 12
#Francisco Llamas
numero=int(input("por favor introduzca un numero"))
a=0
for i in range(1, numero+1):
    if numero%i==0:
        a=a+1
if a==2:
    print("El numero", numero,"es primo")
else:
    print("El numero", numero,"no es primo")

    
