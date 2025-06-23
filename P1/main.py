"""
Este módulo define las clases para un sistema de gestión de biblioteca,
incluyendo la representación de libros y la biblioteca que los gestiona.
"""

class Libro:
    """
    Representa un libro individual en la colección de la biblioteca.

    Atributos:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        disponible (bool): True si el libro está disponible para préstamo, False en caso contrario.
    """
    def __init__(self, titulo: str, autor: str):
        """
        Inicializa un nuevo objeto Libro.

        Args:
            titulo: El título para el nuevo libro.
            autor: El autor del nuevo libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Por defecto, un libro nuevo está disponible.

    def prestar(self) -> bool:
        """
        Intenta prestar el libro. Si está disponible, cambia su estado a no disponible.

        Returns:
            True si el libro fue prestado con éxito, False si ya estaba prestado.
        """
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        """
        Marca el libro como disponible nuevamente.
        """
        self.disponible = True

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del libro, útil para depuración.
        Muestra el título, autor y su estado de disponibilidad.
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro('{self.titulo}', '{self.autor}', Estado: {estado})"


class Biblioteca:
    """
    Representa la biblioteca que gestiona una colección de libros.

    Atributos:
        coleccion (list): Una lista que almacena los objetos Libro de la biblioteca.
    """
    def __init__(self):
        """
        Inicializa una nueva Biblioteca con una colección vacía.
        """
        self.coleccion = []

    def agregar_libro(self, libro: Libro):
        """
        Agrega un nuevo libro a la colección de la biblioteca.

        Args:
            libro: El objeto Libro que se va a agregar.
        """
        self.coleccion.append(libro)
        print(f"Info: El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def buscar_libro(self, titulo: str) -> Libro | None:
        """
        Busca un libro en la colección por su título.

        Args:
            titulo: El título del libro a buscar.

        Returns:
            El objeto Libro si se encuentra, o None si no existe en la colección.
        """
        for libro in self.coleccion:
            if libro.titulo.lower() == titulo.lower(): # Búsqueda no sensible a mayúsculas
                return libro
        return None

    def prestar_libro(self, titulo: str) -> bool:
        """
        Busca un libro por título y, si lo encuentra y está disponible, lo presta.

        Args:
            titulo: El título del libro a prestar.

        Returns:

            True si el préstamo fue exitoso, False en caso contrario (no se encontró o no estaba disponible).
        """
        libro_a_prestar = self.buscar_libro(titulo)
        if libro_a_prestar:
            # El método prestar() del propio libro se encarga de la lógica
            return libro_a_prestar.prestar()
        else:
            # Si el libro no se encuentra, el préstamo no puede realizarse
            return False

# --- Sección de Demostración ---
if __name__ == "__main__":
    # 1. Crear una instancia de la Biblioteca
    mi_biblioteca = Biblioteca()
    print("--- Biblioteca creada. ---")

    # 2. Crear y agregar algunos libros a la colección
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
    libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien")
    libro3 = Libro("1984", "George Orwell")

    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)

    print("\n--- Estado inicial de la colección: ---")
    for libro in mi_biblioteca.coleccion:
        print(libro)

    # 3. Demostrar el préstamo de un libro disponible
    print("\n--- Intentando prestar 'El Señor de los Anillos'... ---")
    titulo_a_prestar = "El Señor de los Anillos"
    if mi_biblioteca.prestar_libro(titulo_a_prestar):
        print(f"✅El libro '{titulo_a_prestar}' ha sido prestado.")
    else:
        print(f"❌No se pudo prestar el libro '{titulo_a_prestar}'.")

    # 4. Verificar el estado del libro después del préstamo
    print("\n--- Estado de la colección después del primer préstamo: ---")
    # Usamos el método de búsqueda para ver un libro en específico
    libro_prestado = mi_biblioteca.buscar_libro(titulo_a_prestar)
    print(f"Búsqueda: {libro_prestado}")

    # 5. Intentar prestar el mismo libro de nuevo (debería fallar)
    print(f"\n--- Intentando prestar '{titulo_a_prestar}' de nuevo... ---")
    if mi_biblioteca.prestar_libro(titulo_a_prestar):
        # Este caso sería un error en nuestra lógica, pero es bueno manejarlo.
        print(f"❌El libro '{titulo_a_prestar}' se pudo prestar dos veces.")
    else:
        # Este es el resultado que esperamos.
        print(f"✅El libro '{titulo_a_prestar}' no se pudo prestar de nuevo, como se esperaba.")

    # 6. Devolver el libro
    print(f"\n--- Devolviendo '{titulo_a_prestar}'... ---")
    libro_devuelto = mi_biblioteca.buscar_libro(titulo_a_prestar)
    if libro_devuelto:
        libro_devuelto.devolver()
        print(f"✅El libro '{titulo_a_prestar}' ha sido devuelto.")
        print(f"   Estado actual: {libro_devuelto}")
    else:
        # Manejamos el caso en que el libro a devolver no se encuentre.
        print(f"❌No se encontró el libro '{titulo_a_prestar}' para devolverlo.")

    # 7. Verificacion de errores o acciones inesperadas
    print("\n--- Verificando el estado de la colección después de la devolución: ---") 
    print("Estado de la colección:")
    for libro in mi_biblioteca.coleccion:
        print(libro)
    
    print("\n--- Prestaremos un libro ---")
    titulo_a_prestar = "El Señor de los Anillos"
    if mi_biblioteca.prestar_libro(titulo_a_prestar):
        print(f"✅El libro '{titulo_a_prestar}' ha sido prestado.")
    else:
        print(f"❌No se pudo prestar el libro '{titulo_a_prestar}'.")

    print("\n--- Volver a prestar el mismo libro ---")
    titulo_a_prestar = "El Señor de los Anillos"
    if mi_biblioteca.prestar_libro(titulo_a_prestar):
        print(f"✅El libro '{titulo_a_prestar}' ha sido prestado.")
    else:
        print(f"❌No se pudo prestar el libro '{titulo_a_prestar}'.")

    
    # 8. Devolver un libro no registrado
    titulo_a_prestar = "El Hobbit"
    print("\n--- Intentando devolver un libro no registrado ---")
    print(f"Intentando devolver '{titulo_a_prestar}'...")
    libro_devuelto = mi_biblioteca.buscar_libro(titulo_a_prestar)
    if libro_devuelto:
        libro_devuelto()
        print(f"✅El libro {titulo_a_prestar} ha sido devuelto.")
    else:
        print(f"❌No se encontró el libro {titulo_a_prestar} para devolverlo.")
