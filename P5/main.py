"""
Este módulo implementa un sistema simple de gestión de evaluación académica
para estudiantes, modelando Exámenes y Estudiantes.
"""

class Examen:
    """
    Representa un examen individual con un tema y una nota.

    Atributos:
        tema (str): El tema del examen (ej. 'POO').
        nota (float): La nota obtenida, validada para estar entre 1.0 y 7.0.
    """
    def __init__(self, tema: str, nota: float):
        """
        Inicializa un nuevo examen.

        Args:
            tema: El tema evaluado.
            nota: La nota obtenida.

        Raises:
            ValueError: Si la nota no está en el rango de 1.0 a 7.0.
        """
        self.tema = tema
        # Validar que la nota esté en el rango permitido.
        if not 1.0 <= nota <= 7.0:
            raise ValueError("La nota debe estar entre 1.0 y 7.0")
        self.nota = nota

    def __repr__(self) -> str:
        """Devuelve una representación legible del examen."""
        return f"Examen(Tema: '{self.tema}', Nota: {self.nota:.1f})"


class Estudiante:
    """
    Representa a un estudiante con su historial de exámenes.

    Atributos:
        nombre (str): El nombre del estudiante.
        examenes (list[Examen]): Lista de exámenes rendidos por el estudiante.
    """
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo estudiante.

        Args:
            nombre: El nombre del estudiante.
        """
        self.nombre = nombre
        self.examenes: list[Examen] = []

    def agregar_examen(self, examen: Examen):
        """Agrega un examen al historial del estudiante."""
        self.examenes.append(examen)
        print(f"Info: Examen de '{examen.tema}' agregado a {self.nombre}.")

    def calcular_promedio(self) -> float:
        """
        Calcula el promedio general de notas de los exámenes rendidos.

        Returns:
            El promedio de las notas, o 0.0 si no hay exámenes.
        """
        # Manejar el caso de que no haya exámenes.
        if not self.examenes:
            return 0.0
        
        total_notas = sum(examen.nota for examen in self.examenes)
        return total_notas / len(self.examenes)

    def mostrar_examenes(self):
        """ Muestra todos los exámenes rendidos por el estudiante."""
        print(f"\n--- Exámenes de {self.nombre} ---")
        if not self.examenes:
            print("No hay exámenes registrados.")
        else:
            for examen in self.examenes:
                print(f"  - {examen}")


# --- Sección de Simulación ---
if __name__ == "__main__":
    print("--- Sistema de Gestión de Evaluación Académica ---")

    # 3. Crear un estudiante
    estudiante_fito = Estudiante("Fito")
    print(f"\nEstudiante creado: {estudiante_fito.nombre}")

    # Agregar al menos dos exámenes
    examen_poo = Examen("POO", 6.5)
    examen_db = Examen("Bases de Datos", 5.8)
    
    estudiante_fito.agregar_examen(examen_poo)
    estudiante_fito.agregar_examen(examen_db)

    # Mostrar los exámenes del estudiante
    estudiante_fito.mostrar_examenes()

    # Imprimir el promedio final
    promedio_fito = estudiante_fito.calcular_promedio()
    print(f"\n=> Promedio final de {estudiante_fito.nombre}: {promedio_fito:.2f}")

    print("\n" + "="*50)
    print("--- Probando casos adicionales ---")

    # Probar el cálculo de promedio sin exámenes
    estudiante_nuevo = Estudiante("Ana")
    print(f"\nEstudiante creado: {estudiante_nuevo.nombre}")
    estudiante_nuevo.mostrar_examenes()
    promedio_ana = estudiante_nuevo.calcular_promedio()
    print(f"=> Promedio de {estudiante_nuevo.nombre} (sin exámenes): {promedio_ana:.2f}")

    # Probar la validación de nota inválida
    print("\nIntentando crear un examen con nota inválida (9.5)...")
    try:
        examen_invalido = Examen("Redes", 9.5)
    except ValueError as e:
        print(f"Error capturado exitosamente: {e}")