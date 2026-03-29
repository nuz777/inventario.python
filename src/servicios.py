"""
Módulo de servicios del inventario
Contiene funciones CRUD y estadísticas
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """Muestra todos los productos"""
    if not inventario:
        print("Inventario vacío")
        return

    for producto in inventario:
        print(f"{producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre"""
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Elimina un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario"""
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }