from src.servicios import *
from src.archivos import *

inventario = []

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
    opcion = input(" Elige una opción: ")

    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Buscar: ")
            print(buscar_producto(inventario, nombre))

        elif opcion == "4":
            nombre = input("Producto: ")
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            actualizar_producto(
                inventario,
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )

        elif opcion == "5":
            nombre = input("Eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print(stats)

        elif opcion == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                decision = input("¿Sobrescribir? (S/N): ").lower()
                if decision == "s":
                    inventario = nuevos
                else:
                    for n in nuevos:
                        existente = buscar_producto(inventario, n["nombre"])
                        if existente:
                            existente["cantidad"] += n["cantidad"]
                            existente["precio"] = n["precio"]
                        else:
                            inventario.append(n)

        elif opcion == "9":
            print("Bye 👋..... hehe")
            break

        else:
            print("Opción inválida")

    except Exception as e:
        print("Error:", e)