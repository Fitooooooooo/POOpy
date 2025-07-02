"""
Este módulo implementa un sistema de agenda digital para gestionar contactos,
permitiendo agregar y buscar contactos por nombre.
"""

class Contacto:
    """
    Representa un contacto con nombre y número de teléfono.

    Atributos:
        nombre (str): El nombre del contacto.
        telefono (str): El número de teléfono del contacto.
    """
    def __init__(self, nombre: str, telefono: str):
        """
        Inicializa un nuevo contacto.

        Args:
            nombre: El nombre de la persona.
            telefono: El número de teléfono.
        """
        self.nombre = nombre
        self.telefono = telefono

    def __repr__(self) -> str:
        """Devuelve una representación legible del contacto."""
        return f"Contacto(Nombre: '{self.nombre}', Teléfono: {self.telefono})"


class Agenda:
    """
    Representa una agenda que almacena y gestiona una lista de contactos.
    """
    def __init__(self):
        """Inicializa una nueva agenda con una lista de contactos vacía."""
        self.contactos: list[Contacto] = []

    def agregar_contacto(self, contacto: Contacto):
        """Agrega un nuevo contacto a la agenda."""
        self.contactos.append(contacto)
        print(f"Info: Contacto '{contacto.nombre}' agregado a la agenda.")

    def buscar_contacto(self, nombre_buscado: str) -> list[str]:
        """
        Busca contactos por nombre exacto y devuelve sus números de teléfono.

        Args:
            nombre_buscado: El nombre a buscar (sensible a mayúsculas/minúsculas).

        Returns:
            Una lista de números de teléfono de los contactos encontrados.
            Devuelve una lista vacía si no se encuentra ningún contacto.
        """
        telefonos_encontrados = [
            contacto.telefono
            for contacto in self.contactos
            if contacto.nombre == nombre_buscado
        ]
        return telefonos_encontrados


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Sistema de Agenda de Contactos ---")

    # 1. Crear una agenda
    mi_agenda = Agenda()

    # 2. Crear y agregar al menos tres contactos (dos con el mismo nombre)
    print("\nAgregando contactos...")
    mi_agenda.agregar_contacto(Contacto("Ana", "555-1234"))
    mi_agenda.agregar_contacto(Contacto("Juan", "555-5678"))
    mi_agenda.agregar_contacto(Contacto("Ana", "555-8765")) # Contacto repetido

    # 3. Demostrar el funcionamiento de la búsqueda
    print("\n--- Realizando búsquedas ---")

    # Búsqueda con múltiples resultados
    print("\nBuscando a 'Ana'...")
    resultados_ana = mi_agenda.buscar_contacto("Ana")
    print(f"Teléfonos encontrados para 'Ana': {resultados_ana}")

    # Búsqueda con un único resultado
    print("\nBuscando a 'Juan'...")
    resultados_juan = mi_agenda.buscar_contacto("Juan")
    print(f"Teléfonos encontrados para 'Juan': {resultados_juan}")

    # Búsqueda sin resultados
    print("\nBuscando a 'Carlos'...")
    resultados_carlos = mi_agenda.buscar_contacto("Carlos")
    print(f"Teléfonos encontrados para 'Carlos': {resultados_carlos}")