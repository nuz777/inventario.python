from src.servicios import *
from src.archivos import *

# Main inventory list (stored in memory)
inventario = []

# Infinite loop to keep the program running
while True:
    def mostrar_menu():
        print("\n" + "="*40)
        print("📦  SISTEMA DE INVENTARIO  📦".center(40))
        print("="*40)
        print("1️⃣  Agregar producto")
        print("2️⃣  Mostrar inventario")
        print("3️⃣  Buscar producto")
        print("4️⃣  Actualizar producto")
        print("5️⃣  Eliminar producto")
        print("6️⃣  Ver estadísticas")
        print("7️⃣  Guardar en CSV")
        print("8️⃣  Cargar desde CSV")
        print("9️⃣  Salir")
        print("="*40)
    mostrar_menu()
#Get user option
    opcion = input("seleccione una opcion: ")

# Handle possible errors to prevent program crash

    try:
# Option 1: Add a new product
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            agregar_producto(inventario, nombre, precio, cantidad)
            
        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion =="3":
            nombre = input("Nombre a buscar: ").lower()
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("producto no encontrado...")

        elif opcion =="4":
            nombre = input("producto a actualizar ")
            nuevo_precio = input("Nuevo precio (enter para omitir )")
            nueva_cantidad = input("Nueva cantidad (Enter para omitir) ")
            actualizado = actualizar_producto (inventario, nombre, float(nuevo_precio)if nuevo_precio else None, int(nueva_cantidad) if nueva_cantidad else None)
            
            if actualizado:
                print("producto actuluazado")
            else:
                print("producto no encontrado...")


        elif opcion == "5":
            nombre = input("Producto a eliminar: ")
            eliminado = eliminar_producto(inventario, nombre)
            if eliminado:
                print("producto eliminado")
            else: 
                print("producto no encontrado...")
# Option 6: Show statistics
        elif opcion == "6":
            estadisticas = calcular_estadisticas(inventario)
            if estadisticas:
                print(f"Unidades totales: {estadisticas['unidades_totales']}")
                print(f"Valor total: ${estadisticas['valor_total']:.2f}")
                print(f"Producto más caro: {estadisticas['producto_mas_caro']['nombre']} (${estadisticas['producto_mas_caro']['precio']:.2f})")
                print(f"Mayor stock: {estadisticas['producto_mayor_stock']['nombre']} ({estadisticas['producto_mayor_stock']['cantidad']} unidades)")
            else:
                print("inventario vacio")


        elif opcion == "7":
            ruta = input("ruta del archivo para guardar:  ")
            guardar_csv(inventario, ruta)
            if ruta:
                print(f"archivo guardado en {ruta}")
            else:
                print("ruta invalida")
# Option 8: Load inventory from CSV file
# Merge or overwrite inventory based on user decision
        elif opcion == 8:
            ruta = input("Ruta del archivo: ")
            nuevos_productos = cargar_csv(ruta)
            if nuevos_productos:
                decision =input("¿ Sobrescribir Inventario (S/N): ").lower()
                if decision == "s":
                    inventario = nuevos_productos
                else:
                    for nuevo in nuevos_productos:
                        existente = buscar_producto(inventario, nuevo["nombre"])
                        if existente:
                            existente["cantidad"]+= nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)
                            print("Archivo cargado exitosamente")

# Exit the program
        elif opcion == "9":
            print("Saliendo del programa...")
            break      

        else:
            print("Opcion no valida, intente de nuevo...")
    except ValueError:
        print("Entrada no valida, por favor ingrese el tipo de dato correcto.")

    except Exception as error:
        print("Ocurrio un error inesperado:", error)
