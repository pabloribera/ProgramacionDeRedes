print("----------------------------------")
print("Practica 05_calculator.py")
print("----------------------------------")
print("Introduce el primer Número: ")
num1=int(input())
print("Introduce el Segundo Número: ")
num2=int(input())


def suma():
    return num1 + num2

def resta():
    return num1 - num2

def multiplicacon():
    return num1 * num2

def division():
    return num1 // num2

def exponencial():
    return num1 ** num2


    



print("¿Que operación quiere hacer?")
print(" *Presione 1 para suma ")
print(" *Presione 2 para resta ")
print(" *Presione 3 para multiplicación ")
print(" *Presione 4 para división ")
print(" *Presione 5 para Exponencial ")


elec= int(input())
print("----------------------------------")
if elec == 1:
    print("La suma total es: " +str(suma))
elif elec == 2:
    print("La resta Total es: " +str(resta))
elif elec == 3:
    print("La multriplicación es: " +str(multiplicacion))
elif elec == 4:
    print("El resultado de la division es: " +str(division))
elif elec == 5:
    print("El resultado exponencial es: " +str(exponencial))
else:
    print("No valido")
print("----------------------------------")    
Resultado={"suma":suma, "resta": resta,"multiplicacion": multiplicacion}




