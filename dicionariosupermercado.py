print("------------------Supermercado XXX registro de inventario--------------------------")
print("!!!******************************************************************************!!!")

print("[1]. Agregar producto")
print("[2]. Mostrar productos")
print("[3]. Editar producto")
print("[4]. Elimonar producto")
print("[0]. Salir")
print("!!!******************************************************************************!!!")

opcion=1
productos=[] #dicionario vacio
while(opcion !=0):
        opcion=int(input("Digita la opcion segun menu indicado: "))
        
        if(opcion==1):
                producto={}
                #datos del diccionario
                producto['codigo']=input("ingrese el codigo del producto: ")
                producto['nombre']= input("ingrese el nombre del producto: ")
                producto['precio']= int(input("ingrese el costo del producto: "))
                productos.append(producto) #lleno la lista
        elif (opcion==2):
                print(productos)
        elif (opcion==3):
                encontrado=True #bandera
                buscarCodigo=input("Digite el codigo que desea buscar")
                for producto in productos:
                    if(producto['codigo']==buscarCodigo):
                            producto['precio']= int(input("ingrese el costo del producto: "))
                            encontrado=True #bandera
                            break
                    else:
                        encontrado=False
                if(encontrado==False):
                        print("codigo no existe")
        elif (opcion==4):
                        buscarCodigo=input("Digite el codigo que desea eliminar")
                        del(productos[producto]) #eliminar elementos del diccionario
                        print("producto eliminado con exito!")
                        print(producto['codigo'], producto['nombre'], producto['precio'])
        else:
            print("producto no existe")
                                


       