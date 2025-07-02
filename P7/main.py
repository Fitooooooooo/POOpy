"""
Este módulo implementa un sistema básico de pedidos para una tienda,
gestionando productos y el cálculo del total de los pedidos.
"""

class Producto:
    """
    Representa un producto con su nombre y precio.

    Atributos:
        nombre (str): El nombre del producto.
        precio (float): El precio del producto, debe ser positivo.
    """
    def __init__(self, nombre: str, precio: float):
        """
        Inicializa un nuevo producto.

        Args:
            nombre: El nombre del producto.
            precio: El precio del producto.

        Raises:
            ValueError: Si el precio es menor o igual a cero.
        """
        self.nombre = nombre
        if precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self.precio = precio

    def __repr__(self) -> str:
        """Devuelve una representación legible del producto."""
        return f"Producto(Nombre: '{self.nombre}', Precio: ${self.precio:,.2f})"


class Pedido:
    """
    Representa un pedido que contiene una lista de productos.
    """
    def __init__(self):
        """Inicializa un nuevo pedido con una lista de productos vacía."""
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        """Agrega un producto a la lista del pedido."""
        self.productos.append(producto)
        print(f"Info: '{producto.nombre}' agregado al pedido.")

    def calcular_total(self) -> float:
        """Calcula y devuelve la suma total de los precios de los productos."""
        return sum(producto.precio for producto in self.productos)

    def mostrar_resumen(self):
        """ Muestra un resumen detallado del pedido."""
        print("\n--- Resumen del Pedido ---")
        if not self.productos:
            print("El pedido está vacío.")
        else:
            for producto in self.productos:
                print(f"  - {producto.nombre}: ${producto.precio:,.2f}")
        print("-" * 25)
        print(f"Total a pagar: ${self.calcular_total():,.2f}")


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Sistema de Pedidos de la Tienda ---")

    # 2. Crear un pedido nuevo y agregar tres productos
    mi_pedido = Pedido()
    print("\nAgregando productos predefinidos...")
    mi_pedido.agregar_producto(Producto("Laptop Gamer", 1550.99))
    mi_pedido.agregar_producto(Producto("Mouse RGB", 45.50))
    mi_pedido.agregar_producto(Producto("Monitor Curvo 27\"", 320.00))

    # 3. Mostrar el total del pedido
    print(f"\nEl total del pedido es: ${mi_pedido.calcular_total():,.2f}")

    #  Mostrar el resumen completo
    mi_pedido.mostrar_resumen()

    print("\n" + "="*50)
    print("--- Creación de Pedido Interactivo ---")

    pedido_interactivo = Pedido()
    while True:
        nombre_prod = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_prod.lower() == 'fin':
            break
        try:
            precio_prod_str = input(f"Ingrese el precio para '{nombre_prod}': ")
            precio_prod = float(precio_prod_str)
            pedido_interactivo.agregar_producto(Producto(nombre_prod, precio_prod))
        except ValueError as e:
            print(f"Error: Dato inválido. {e}. Intente de nuevo.")

    # Mostrar resumen del pedido interactivo si se agregaron productos
    if pedido_interactivo.productos:
        pedido_interactivo.mostrar_resumen()