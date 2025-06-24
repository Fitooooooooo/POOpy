"""
Este módulo simula el funcionamiento básico de un cajero automático
y las cuentas bancarias asociadas.
"""

class CuentaBancaria:
    """
    Representa una cuenta bancaria con un saldo y número de cuenta.

    Atributos:
        numero_cuenta (str): Identificador único de la cuenta.
        saldo (float): Saldo disponible en la cuenta.
    """
    def __init__(self, numero_cuenta: str, saldo_inicial: float):
        """
        Inicializa una nueva cuenta bancaria.

        Args:
            numero_cuenta: El número de la cuenta.
            saldo_inicial: El saldo con el que se crea la cuenta.
        """
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def retirar(self, monto: float) -> bool:
        """
        Intenta retirar un monto de la cuenta.

        Args:
            monto: La cantidad de dinero a retirar.

        Returns:
            True si el retiro fue exitoso, False si los fondos son insuficientes.
        """
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            return True
        return False

    def __repr__(self) -> str:
        return f"Cuenta(Nº: {self.numero_cuenta}, Saldo: ${self.saldo:,.2f})"


class CajeroAutomatico:
    """
    Representa un cajero automático que interactúa con cuentas bancarias.
    """
    def realizar_retiro(self, cuenta: CuentaBancaria, monto: float) -> str:
        """
        Procesa una solicitud de retiro para una cuenta específica.

        Args:
            cuenta: La cuenta bancaria de la que se retirará el dinero.
            monto: El monto a retirar.

        Returns:
            Un mensaje de estado indicando el resultado de la operación.
        """
        if cuenta.retirar(monto):
            return f"Retiro exitoso. Nuevo saldo: ${cuenta.saldo:,.2f}"
        else:
            return f"Fondos insuficientes. No se pudo completar el retiro de ${monto:,.2f}."


def mostrar_saldo(cuenta: CuentaBancaria):
    """
    Función auxiliar para imprimir el estado de una cuenta.
    """
    print(f"Estado de la cuenta -> {cuenta}")


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Simulación de Cajero Automático ---")

    # 1. Crear dos cuentas bancarias con saldos distintos
    cuenta1 = CuentaBancaria("12345-6", 50000.0)
    cuenta2 = CuentaBancaria("98765-4", 15000.0)

    # Crear una instancia del cajero
    cajero = CajeroAutomatico()

    print("\n--- Saldos Iniciales ---")
    mostrar_saldo(cuenta1)
    mostrar_saldo(cuenta2)

    # 2. Simular tres operaciones de retiro
    print("\n--- Operaciones de Retiro ---")

    # a) Retiro exitoso
    print("\n1. Retiro exitoso de $10,000 de la cuenta 1:")
    print(cajero.realizar_retiro(cuenta1, 10000.0))
    mostrar_saldo(cuenta1)

    # b) Intento de retiro con monto mayor al saldo
    print("\n2. Intento de retiro de $20,000 de la cuenta 2 (saldo $15,000):")
    print(cajero.realizar_retiro(cuenta2, 20000.0))
    mostrar_saldo(cuenta2)

    # c) Retiro que reduce el saldo a cero
    print("\n3. Retiro de $15,000 de la cuenta 2 para dejar saldo en cero:")
    print(cajero.realizar_retiro(cuenta2, 15000.0))
    mostrar_saldo(cuenta2)