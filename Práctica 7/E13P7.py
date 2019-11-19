"""Escribe un programa que le pida al usuario si quiere calcular si un número
es primo con for o con while, por tanto, habrán dos funciones que
se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks)
, o de otra (con while). Ambas funciones devolverá true (si es es primo) o false
(si no es primo). El programa principal informará del resultado. Además, como me
jora puedes calcular el tiempo que tarda en encontrar la solución de una manera
u otra."""
#Francisco Llamas
def f(numero):
    if inicio=="F":
        for i in range(1, numero):
            if numero%i==0:
                print("su numero es primo")
                return True 
            else:
                print("su muero no es primo")
                return False
    elif inicio=="W":
        while numero%i==0:
            print("su numero es primo")
            return True
        print("su numero no es primo")
        return False

#prog principal
inicio=input("por favor, digame si quiere calcular si es primo con for(F) o while(W)")
numero=int(input("por favor, introduzca su numero"))
f(numero)
