import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV"""
    if not inventario:
        print("No hay datos para guardar")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar:", e)
    

def cargar_csv(ruta):
    """Carga un inventario desde CSV"""
    inventario = []
    errores = 0 

    try:
        with open(ruta, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return []

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"{errores} filas inválidas omitidas")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print("Error:", e)

    return []