'''Construir un programa que permita ingresar N (cantidad digitada por el
usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
ingresados (+1)'''

numeros=[]
tamano=int(input("Ingrese el tamaño de la lista:"))
multiplo2=0
multiplo3=0

for i in range(tamano):
        numero=int(input("Ingrese el número de la lista:"))
        numeros.append(numero)
        if (numero%2==0):
            multiplo2+=1
            print("El numero es  multiplo de 2")
        elif ( numero%3==0 ):
            print("El numero es multiplo de 3")
            multiplo3+=1
        else:
            print(" es multiplo de otro numero")
print(f" {numeros}")
print(f"la cantidad de multiplos de 2 es: {multiplo2}")   
print(f"la cantidad de multiplos de 2 es {multiplo3}")