print("----------------------------------")
print("Practica 05_calculator.py")
print("----------------------------------")
print("Introduce el primer Número: ")
num1 = int(input())
print("Introduce el Segundo Número: ")
num2 = int(input())


def suma():
    return num1 + num2

def resta():
    return num1 - num2

def multiplicacion():
    return num1 * num2

def division():
    return num1 // num2

def exponencial():
    return num1 ** num2

operaciones={"Suma": 1, "Resta": 2, "Multiplicacion": 3, "Division": 4, "Exponencial": 5}

print("¿Que operación quiere hacer?")
print(" *Presione 1 para Suma ")
print(" *Presione 2 para Resta ")
print(" *Presione 3 para Multiplicación ")
print(" *Presione 4 para División ")
print(" *Presione 5 para Exponencial ")


print("----------------------------------")
def resultado():
    elec = int(input())
    if elec == 1:
        print("La suma total es: " + str(suma()))
    elif elec == 2:
        print("La resta Total es: " + str(resta()))
    elif elec == 3:
        print("La multriplicación es: " + str(multiplicacion()))
    elif elec == 4:
        print("El resultado de la division es: " + str(division()))
    elif elec == 5:
        print("El resultado exponencial es: " + str(exponencial()))
    else:
        print("No valido")
    print("----------------------------------")
resultado()
print("----------------------------------")
print(operaciones)