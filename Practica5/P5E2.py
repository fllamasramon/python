#Francisco Llamas Ramon
#Práctia 5 ejercicio 2
n1=int(input("por favor, escriba un número"))
n2=int(input("por favor, escriba otro número"))
for i in range(n1, (n2+1)):
       if i%2==0:
              print("El número", i,"es par")
       else:
              print("El número", i,"es impar")
if n1>n2:
       for i in range(n2, (n1+1)):
              if i%2==0:
                     print("El número", i,"es par")
              else:
                     print("El número", i,"es impar")

        
    
