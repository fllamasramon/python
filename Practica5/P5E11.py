#Práctica 5 ejercicio 11
#Francisco Llamas
numero=int(input("por favor introduzca un número"))
for i in range(1, numero+1):
    if numero%i==0:
        print(i, "es divisor de", numero)
  
