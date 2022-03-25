'''-Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
inverso al ingresado+(1)'''

salpicon=["papaya", "mango", "banano","fresa", "quiwi", "manzana", "pera", "durazno","melon","cereza"]
print(salpicon)

for fruta in reversed(salpicon):
    print(fruta)


# otra forma con len que me da la longitud de la lista
salpico = ["papaya", "mango", "banano","fresa", "quiwi", "manzana", "pera", "durazno","melon","cereza"]
print(salpicon)
listafrutas = len(salpicon)
for i in range(listafrutas):
      print(salpicon[listafrutas-i-1])