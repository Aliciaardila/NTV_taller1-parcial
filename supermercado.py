print("------------------Supermercado XXX registro de inventario--------------------------")
print("!!!******************************************************************************!!!")

print("1. Agregar producto)")
print("2. Mostrar productos")
print("3. Editar producto")
print("4. Elimonar producto")
print("0. Salir")
print("!!!******************************************************************************!!!")

opcion=1
productos=[]


while(opcion!=0):
           
         opcion=int(input("Digita 1 para ingresar el producto, 2 para listar productos:"))
                   
         if(opcion==1):
                codigo=int(input("Digite codigo del producto:"))
                nombre=input("Digite nombre del producto:")
                precio=float(input("Digite precio del producto:"))
                producto ={'nombre':nombre, 'codigo':codigo, 'precio':precio}
                productos.append(producto)
         elif(opcion==2):
                print(productos)
                opcion =int((input("Ingrese el numero 3 para buscar por codigo y modificar o 4 para eliminar: ")))
             
         elif (opcion==3):
                bandera=True
                codigoBuscar=int(input("Ingrese el codigo del producto a buscar : "))
                for producto in productos:
                    if codigoBuscar == (producto['codigo']):
                        print(producto['codigo'], producto['nombre'], producto['precio'])
                        seleccionCambio=int((input("1, para combiar codigo, 2 para cambiar nombre, y 3 para cambiar precio, y 4 para eliminar el producto ")))
                    elif seleccionCambio == 1:
                            codigoNuevo=int(input("Ingrese el nuevo codigo: "))
                            producto['codigo'] = codigoNuevo
                            print(producto)
                            print("Cambio guardado con exito!")
                            opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar y modificar productos")))
                    elif seleccionCambio == 2:
                            nombreNuevo=input("Ingrese el nuevo nombre: ")
                            producto['nombre'] = nombreNuevo
                            print(producto)
                            print("Cambio guardado con exito!")
                            opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar y modificar productos")))  
                    elif seleccionCambio == 3:
                            precio_nuevo=int(input("Ingrese el precio codigo: "))
                            producto['precio'] = precio_nuevo
                            print(producto)
                            print("Cambio guardado con exito!")
                            opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar y modificar productos")))
                    elif seleccionCambio == 4:
                        del(productos[producto])
                       
                        print("producto eliminado con exito!")
                        opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto")))
                        print(producto['codigo'], producto['nombre'], producto['precio']) 
                else: 
                 print(f"Digite una opcion valida")