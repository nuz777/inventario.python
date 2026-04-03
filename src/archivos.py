import csv
# Import CSV module to handle file operations

def guardar_csv(inventario, ruta, incluir_header=True):
    """"Guardar el inventario en un archivo CSV"""
    if not inventario:
        print("inventario vacio, no se guardara el archivo")
        return
    # Open file in write mode
    try: 
        # Open file in write mode
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
        # Write header row
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
        # Write product rows
            for producto in inventario:
                writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])

        print(f"Inventario guardado en {ruta}")
    
    except Exception as e:
        print("Error al guardar el archivo:", e)

# List to store loaded products
def cargar_csv(ruta):
    """"Carga un inventario desde un archivo CSV"""
    inventario = []
    erroes = 0

    try:
        # Open file in read mode ("r")
        with open(ruta, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            # Read the header (first row of the file)
            if header != ["nombre", "precio", "cantidad"]:
                print("Formato de archivo no valido")
                return []
            
            for fila in reader:
                try: # Try block to validate each row individually
                    if len(fila) != 3:
                        raise ValueError("Fila con formato incorrecto")
                    # Ensure row has exactly 3 columns
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    if precio < 0 or cantidad < 0: # Validate that values are not negative
                        raise ValueError("Precio y cantidad deben ser no negativos")  # Add valid product to the list
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except:
                    erroes += 1 # If any error occurs in the row, count it as invalid
                    print(f"{erroes} fila con formato incorrect0") # Continue processing remaining rows without stopping
                    return inventario
# Handle case where file does not exist
    except FileNotFoundError:
        print("Archivo no encontrado")
# Handle unexpected errors during file reading       
    except Exception as e:
        print("Error al cargar el archivo:", e) 

# Always return a list to avoid breaking the program
    return []    
                            