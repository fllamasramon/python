#Francisco Llamas
#Práctica 4 ejercicio 1
a=int(input("introduzca un numero"))
b=int(input("introduzca un numero"))
c=int(input("introduzca un numero"))
d=int(input("introduzca un numero"))
e=int(input("introduzca un numero"))
if a >=b and a >=c and a >=d and a >=e:
    print("el numero", a,"es el mayor")
elif b >=a and b >=c and b >=d and b >=e:
    print("el numero", b,"es el mayor")
elif c >=a and c >=b and c >=d and c >=e:
    print("el numero", c,"es el mayor")
elif d >=a and d >=b and d >=c and d >=e:
    print("el numero", d,"es el mayor")
elif e >=a and e >=b and e >=c and e >=d:
    print("el numero", e,"es el mayor")
if a <=b and a <=c and a <=d and a <=e:
    print("el numero", a,"es el menor")
elif b <=a and b <=c and b <=d and b <=e:
    print("el numero", b,"es el menor")
elif c <=a and c <=b and c <=d and c <=e:
    print("el numero", c,"es el menor")
elif d <=a and d <=b and d <=c and d<=e:
    print("el numero", d,"es el menor")
elif e <=a and e <=b and e <=c and e<=d:
    print("el numero", d,"es el menor")
if a==b and a==b and a==c and a==d and a==e:
    print("todos los numeros son iguales")
    
