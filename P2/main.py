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

# --- Sección de Simulación para la Clase Habitacion ---
# --- ✅ : Resultado bueno   ❌: Resultado malo---
if __name__ == "__main__":
    print("--- Probando la clase Habitacion ---")

    # 1. Crear una habitación. Su estado inicial debe ser "Disponible".
    h101 = Habitacion(101)
    print(f"Estado inicial: {h101}")

    # 2. Intentar reservar la habitación. Debe ser exitoso y el estado cambiar a "Ocupada".
    print("\nIntentando primera reserva...")
    if h101.reservar():
        print("✅ Reserva exitosa (el método devolvió True).")
    else:
        print("❌ Fallo inesperado en la reserva.")
    print(f"Estado después de la reserva: {h101}")

    # 3. Intentar reservar la misma habitación de nuevo. Debe fallar.
    print("\nIntentando segunda reserva en la misma habitación...")
    if h101.reservar():
        print("❌ Error: La habitación se pudo reservar dos veces.")
    else:
        print("✅ Correcto: La reserva falló (el método devolvió False) porque ya estaba ocupada.")

    # 4. Liberar la habitación. El estado debe volver a "Disponible".
    print("\nLiberando la habitación...")
    h101.liberar()
    print(f"Estado final: {h101}")
