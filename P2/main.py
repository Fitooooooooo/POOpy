"""
Este módulo define las clases para un sistema de gestión de reservas de hotel.
"""
from __future__ import annotations

class Habitacion:
    """
    Representa una habitación individual en el hotel.

    Atributos:
        numero (int): El número que identifica la habitación.
        ocupada (bool): True si la habitación está ocupada, False si está disponible.
    """
    def __init__(self, numero: int):
        """
        Inicializa una nueva habitación.

        Args:
            numero: El número de la habitación.
        """
        self.numero = numero
        self.ocupada = False  # Inicialmente, todas las habitaciones están libres.

    def reservar(self) -> bool:
        """
        Intenta reservar la habitación. Si está libre, la marca como ocupada.

        Returns:
            True si la reserva fue exitosa, False si ya estaba ocupada.
        """
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        """
        Marca la habitación como disponible nuevamente.
        """
        self.ocupada = False

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena de la habitación.
        """
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitacion(Nº: {self.numero}, Estado: {estado})"


class Cliente:
    """
    Representa a un cliente del hotel.

    Atributos:
        nombre (str): El nombre del cliente.
        habitacion_asignada (Habitacion | None): La habitación reservada por el cliente.
    """
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo cliente.

        Args:
            nombre: El nombre del cliente.
        """
        self.nombre = nombre
        self.habitacion_asignada: Habitacion | None = None

    def hacer_reserva(self, habitacion: Habitacion) -> str:
        """
        Intenta realizar una reserva para el cliente en una habitación específica.

        Args:
            habitacion: El objeto Habitacion que se intentará reservar.

        Returns:
            Un mensaje indicando el resultado de la operación.
        """
        if habitacion.reservar():
            self.habitacion_asignada = habitacion
            return f"Habitación {habitacion.numero} reservada para {self.nombre}"
        else:
            return "No se pudo reservar"

    def liberar_reserva(self) -> str:
        """
        Libera la habitación asignada al cliente, si es que tiene una.
        Esto actualiza tanto el estado de la habitación como el del cliente.

        Returns:
            Un mensaje indicando el resultado de la operación.
        """
        if self.habitacion_asignada:
            numero_habitacion = self.habitacion_asignada.numero
            self.habitacion_asignada.liberar()
            self.habitacion_asignada = None
            return f"Reserva de la habitación {numero_habitacion} liberada por {self.nombre}."
        else:
            return f"{self.nombre} no tiene ninguna habitación para liberar."

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del cliente y su reserva."""
        if self.habitacion_asignada:
            return f"Cliente('{self.nombre}', Habitación: {self.habitacion_asignada.numero})"
        else:
            return f"Cliente('{self.nombre}', Sin reserva)"

# --- Sección de Simulación del Sistema Completo ---
if __name__ == "__main__":
    print("--- Simulación del Sistema de Reservas de Hotel ---")

    # 1. Crear una habitación y un cliente, como pide el escenario.
    h101 = Habitacion(101)
    cliente_juan = Cliente("Juan")
    print(f"Situación inicial: {h101}, {cliente_juan}")

    # 2. Juan reserva la habitación disponible.
    print("\n--- Juan intenta reservar la habitación 101 ---")
    mensaje = cliente_juan.hacer_reserva(h101)
    print(f"Resultado: {mensaje}")
    print(f"Situación después de la reserva: {h101}, {cliente_juan}")

    # 3. Un segundo cliente intenta reservar la misma habitación (debe fallar).
    print("\n--- Ana intenta reservar la habitación 101 (ya ocupada) ---")
    cliente_ana = Cliente("Ana")
    mensaje_ana = cliente_ana.hacer_reserva(h101)
    print(f"Resultado para Ana: {mensaje_ana}")
    print(f"Situación (no debe cambiar): {h101}, {cliente_ana}")

    # 4. Juan libera su habitación.
    print("\n--- Juan libera su reserva ---")
    mensaje_liberar = cliente_juan.liberar_reserva()
    print(f"Resultado: {mensaje_liberar}")
    print(f"Situación final: {h101}, {cliente_juan}")
