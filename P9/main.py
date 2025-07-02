"""
Este módulo implementa un sistema básico de inventario para una tienda,
gestionando productos y su stock.
"""

class Producto:
    """
    Representa un producto con su nombre y cantidad disponible.

    Atributos:
        nombre (str): El nombre único del producto.
        cantidad (int): La cantidad de unidades en stock.
    """
    def __init__(self, nombre: str, cantidad: int):
        """
        Inicializa un nuevo producto.

        Args:
            nombre: El nombre del producto.
            cantidad: La cantidad inicial del producto.
        
        Raises:
            ValueError: Si la cantidad inicial es negativa.
        """
        self.nombre = nombre
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = cantidad

    def agregar_stock(self, cantidad_adicional: int):
        """Aumenta la cantidad de stock del producto."""
        if cantidad_adicional > 0:
            self.cantidad += cantidad_adicional

    def __repr__(self) -> str:
        """Devuelve una representación legible del producto."""
        return f"Producto(Nombre: '{self.nombre}', Stock: {self.cantidad} unidades)"


class Inventario:
    """
    Gestiona una colección de productos utilizando un diccionario.
    """
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.productos: dict[str, Producto] = {}

    def agregar_producto(self, producto_nuevo: Producto):
        """
        Agrega un producto al inventario. Si ya existe, suma su cantidad.
        """
        if producto_nuevo.nombre in self.productos:
            print(f"Info: '{producto_nuevo.nombre}' ya existe. Agregando {producto_nuevo.cantidad} unidades al stock.")
            self.productos[producto_nuevo.nombre].agregar_stock(producto_nuevo.cantidad)
        else:
            print(f"Info: Agregando nuevo producto '{producto_nuevo.nombre}' al inventario.")
            self.productos[producto_nuevo.nombre] = producto_nuevo

    def consultar_stock(self, nombre_producto: str) -> int:
        """
        Consulta la cantidad disponible de un producto.

        Returns:
            La cantidad en stock del producto, o 0 si no existe.
        """
        producto = self.productos.get(nombre_producto)
        return producto.cantidad if producto else 0

    def mostrar_inventario(self):
        """Muestra el estado completo del inventario."""
        print("\n--- Estado Actual del Inventario ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"- {producto}")
        print("-" * 35)


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Sistema de Inventario de Productos ---")
    
    mi_inventario = Inventario()

    print("\n1. Agregando productos nuevos al inventario...")
    mi_inventario.agregar_producto(Producto("Laptop", 10))
    mi_inventario.agregar_producto(Producto("Mouse", 50))
    mi_inventario.mostrar_inventario()

    print("\n2. Agregando stock a un producto existente (caso repetido)...")
    mi_inventario.agregar_producto(Producto("Laptop", 5))
    mi_inventario.mostrar_inventario()

    print("\n3. Consultando stock...")
    print(f"Stock de 'Laptop': {mi_inventario.consultar_stock('Laptop')}")
    print(f"Stock de 'Mouse': {mi_inventario.consultar_stock('Mouse')}")
    print(f"Stock de 'Teclado' (inexistente): {mi_inventario.consultar_stock('Teclado')}")