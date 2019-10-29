#Francisco Llamas Ramón
#Ejercicio 7 práctica 7
dia=int(input("introduzca el día deseado"))
mes=int(input("introduzca el mes deseado"))
if dia<1 or dia>31:
    print("el dia no es correcto")
elif mes<1 or mes>12:
    print("el mes no es correcto")
elif mes==2 and dia >28:
    print("fecha incorrecta")
elif mes==4 or mes==6 or mes==9 or mes==11:
    print("fecha incorrecta")
else:
    print("Su fecha es valida")
    
    

    
    
