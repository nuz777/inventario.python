
from src.servicios import *
from src.archivos import *
from colorama import Fore, Style, init
init()

inventario = []

def mostrar_menu():

    print(Fore.CYAN + "═"*50)
    print(Fore.YELLOW + "📦  SISTEMA DE INVENTARIO  📦".center(50))
    print(Fore.CYAN + "═"*50)

    print(Fore.GREEN + "  [1] ➤ Agregar producto")
    print("  [2] ➤ Mostrar inventario")
    print("  [3] ➤ Buscar producto")
    print("  [4] ➤ Actualizar producto")
    print("  [5] ➤ Eliminar producto")
    print("  [6] ➤ Ver estadísticas")
    print("  [7] ➤ Guardar en CSV")
    print("  [8] ➤ Cargar desde CSV")
    print(Fore.RED + "  [9] ➤ Salir")

    print(Fore.CYAN + "═"*50)
    print(Style.RESET_ALL)
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ➤  ")

    try:
# Option 1: Add a new product
        if opcion == "1":

            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = float(input("Cantidad: "))

            agregado = agregar_producto(inventario, nombre, precio, cantidad)
            if agregado is not None:
                print("Producto agregado exitosamente.")
                
            else:
                print("Error al agregar el producto.")

            

# Option 2: Show inventory   
        elif opcion == "2":
            print("-----Inventario Actual-----".center(50))
            mostrar_inventario(inventario)

# Option 3: Search for a product by name
        elif opcion =="3":

            nombre = input("Nombre a buscar: ").lower()
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("producto no encontrado...")
            
# Option 4: Update product details
        elif opcion =="4":

            nombre = input("producto a actualizar ")
            nuevo_precio = input("Nuevo precio (enter para omitir )")
            nueva_cantidad = input("Nueva cantidad (Enter para omitir) ")
            actualizado = actualizar_producto (inventario, nombre, float(nuevo_precio)if nuevo_precio else None, float(nueva_cantidad) if nueva_cantidad else None)
            
            if actualizado:
                print("producto actuluazado")
            else:
                print("producto no encontrado...")


# Option 5: Remove a product from the inventory
        elif opcion == "5":

            nombre = input("Producto a eliminar: ")
            eliminado = eliminar_producto(inventario, nombre)
            if eliminado:
                print("producto eliminado")
            else: 
                print("producto no encontrado...")

# Option 6: Show statistics
        elif opcion == "6":

            print("-----Estadísticas del Inventario-----".center(50))

            estadisticas = calcular_estadisticas(inventario)
            if estadisticas:
                print(f"Unidades totales: {estadisticas['unidades_totales']}")
                print(f"Valor total: ${estadisticas['valor_total']:.2f}")
                print(f"Producto más caro: {estadisticas['producto_mas_caro']['nombre']} (${estadisticas['producto_mas_caro']['precio']:.2f})")
                print(f"Mayor stock: {estadisticas['producto_mayor_stock']['nombre']} ({estadisticas['producto_mayor_stock']['cantidad']} unidades)")
            else:
                print("inventario vacio")
            

        elif opcion == "7":

            if not inventario:
                print("No hay productos en el inventario para guardar.")
            else:
                print("-----Guardado inventario en CSV-----")
                ruta = input("Ruta del archivo engrese el nombre  finalizando con .csv  (archivo.csv): ")
                guardar_csv(inventario, ruta)
            

#  Load inventory from CSV file
        elif opcion == 8:

            ruta = input("Ruta del archivo: ")
            nuevos_productos = cargar_csv(ruta)
            if nuevos_productos:
                decision =input("¿ Sobrescribir Inventario (S/N): ").lower()   # Merge or overwrite inventory based on user decision
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
            print("\nERROR: Opción no válida.")

    except ValueError:
        print("Entrada no valida, por favor ingrese el tipo de dato correcto.")

    except Exception as error:
        print("Ocurrio un error inesperado:", error)
