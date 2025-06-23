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

