"""
Este módulo implementa un sistema de empleados y nómina, demostrando
el uso de herencia para extender funcionalidades con bonos.
"""
from __future__ import annotations

class Empleado:
    """
    Clase base que representa a un empleado con un salario fijo.

    Atributos:
        nombre (str): El nombre del empleado.
        salario_base (float): El salario base mensual del empleado.
    """
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self) -> float:
        """Calcula el pago mensual, que es simplemente el salario base."""
        return self.salario_base

    def __repr__(self) -> str:
        """Devuelve una representación legible del empleado."""
        return f"Empleado(Nombre: '{self.nombre}', Salario: ${self.salario_base:,.2f})"


class EmpleadoConBono(Empleado):
    """
    Representa a un empleado que recibe un bono adicional.
    Hereda de la clase Empleado.
    """
    def __init__(self, nombre: str, salario_base: float, bono: float):
        # Se llama al constructor de la clase padre (Empleado) para inicializar
        # los atributos comunes (nombre y salario_base).
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_pago(self) -> float:
        """
        Sobrescribe el método de la clase padre para calcular el pago,
        sumando el bono al salario base.
        """
        pago_base = super().calcular_pago()
        return pago_base + self.bono

    def __repr__(self) -> str:
        """Devuelve una representación más específica para este tipo de empleado."""
        return f"EmpleadoConBono(Nombre: '{self.nombre}', Salario: ${self.salario_base:,.2f}, Bono: ${self.bono:,.2f})"


class Nomina:
    """
    Gestiona una lista de empleados y calcula el total de la nómina.
    """
    def __init__(self):
        """Inicializa una nómina con una lista de empleados vacía."""
        self.empleados: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado):
        """Agrega un empleado (de cualquier tipo) a la nómina."""
        self.empleados.append(empleado)
        print(f"Info: Empleado '{empleado.nombre}' agregado a la nómina.")

    def calcular_nomina_total(self) -> float:
        """
        Calcula el costo total de la nómina sumando el pago de cada empleado.
        """
        return sum(empleado.calcular_pago() for empleado in self.empleados)


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Sistema de Empleados y Nómina ---")

    # Crear empleados de diferentes tipos
    emp_regular = Empleado("Carlos", 3000.0)
    emp_con_bono = EmpleadoConBono("Ana", 4000.0, 500.0)

    # Crear la nómina y agregar a los empleados
    nomina_empresa = Nomina()
    print("\nAgregando empleados a la nómina...")
    nomina_empresa.agregar_empleado(emp_regular)
    nomina_empresa.agregar_empleado(emp_con_bono)

    # Calcular y mostrar la nómina total
    total_a_pagar = nomina_empresa.calcular_nomina_total()
    print("\n---------------------------------")
    print(f"Total de la nómina a pagar (Carlos $3000 + Ana $4500): ${total_a_pagar:,.2f}")
    print("---------------------------------")