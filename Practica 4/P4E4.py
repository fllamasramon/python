#Práctica 4 ej 4
#Francisco Llamas
n1=int(input("introduzca un numero"))
n2=int(input("introduzca un numero"))
n3=int(input("introduzca un numero"))
n4=int(input("introduzca un numero"))
if n4%n3==0 and n4%n2==0 and n4%n1==0:
    print("el número", n4,"es divisor de los números", n3, n2, n1)
else:
    print("el número", n4,"no es divisor de los números", n3, n2, n1)
