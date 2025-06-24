"""
Este módulo define las clases para un sistema de gestión de inscripciones
de una universidad, manejando estudiantes y cursos.
"""
from __future__ import annotations


class Curso:
    """
    Representa un curso ofrecido por la universidad.

    Atributos:
        nombre (str): El nombre del curso.
        estudiantes_inscritos (list[Estudiante]): Lista de estudiantes inscritos en el curso.
    """
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo curso.

        Args:
            nombre: El nombre del curso (ej. "Cálculo I").
        """
        self.nombre = nombre
        # Cada curso empieza con una lista vacía de estudiantes.
        self.estudiantes_inscritos: list['Estudiante'] = []

    def inscribir_estudiante(self, estudiante: Estudiante):
        """
        Inscribe un estudiante en este curso, manejando la relación bidireccional.
        Esta es la fuente de verdad para una inscripción.

        Args:
            estudiante: El objeto Estudiante a inscribir.
        """
        # Evita inscripciones duplicadas (Consideración adicional)
        if estudiante not in self.estudiantes_inscritos:
            self.estudiantes_inscritos.append(estudiante)
            # Asegura la consistencia: añade este curso a la lista del estudiante
            estudiante.cursos_inscritos.append(self)
            print(f"Inscripción exitosa: '{estudiante.nombre}' en '{self.nombre}'.")

    def dar_de_baja_estudiante(self, estudiante: Estudiante):
        """
        Da de baja a un estudiante de este curso, manejando la relación bidireccional.

        Args:
            estudiante: El objeto Estudiante a dar de baja.
        """
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)
            # Asegura la consistencia: elimina este curso de la lista del estudiante
            estudiante.cursos_inscritos.remove(self)
            print(f"Baja exitosa: '{estudiante.nombre}' del curso '{self.nombre}'.")
        else:
            print(f"Advertencia: '{estudiante.nombre}' no estaba inscrito en '{self.nombre}'.")

    def __repr__(self) -> str:
        return f"Curso('{self.nombre}')"


class Estudiante:
    """
    Representa a un estudiante de la universidad.

    Atributos:
        nombre (str): El nombre del estudiante.
        cursos_inscritos (list[Curso]): Lista de cursos en los que el estudiante está inscrito.
    """
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo estudiante.

        Args:
            nombre: El nombre del estudiante.
        """
        self.nombre = nombre
        # Cada estudiante empieza sin cursos inscritos.
        self.cursos_inscritos: list[Curso] = []

    def inscribir_en_curso(self, curso: Curso):
        """
        Permite al estudiante iniciar el proceso de inscripción en un curso.
        Delega la lógica al método del curso para mantener la consistencia.
        """
        curso.inscribir_estudiante(self)

    def __repr__(self) -> str:
        return f"Estudiante('{self.nombre}')"


# --- Sección de Simulación ---
if __name__ == "__main__":
    # b) Crear al menos tres cursos y cuatro estudiantes
    print("--- Creando Cursos y Estudiantes ---")
    curso_calculo = Curso("Cálculo I")
    curso_fisica = Curso("Física General")
    curso_poo = Curso("Programación Orientada a Objetos")

    estudiante_ana = Estudiante("Ana Garcia")
    estudiante_juan = Estudiante("Juan Perez")
    estudiante_clara = Estudiante("Clara Soto")
    estudiante_pedro = Estudiante("Pedro Pascal")

    print("Cursos creados:", curso_calculo, curso_fisica, curso_poo)
    print("Estudiantes creados:", estudiante_ana, estudiante_juan, estudiante_clara, estudiante_pedro)
    print("\n--- Proceso de Inscripción ---")

    # Inscribir a los estudiantes en distintos cursos
    estudiante_ana.inscribir_en_curso(curso_calculo)
    estudiante_ana.inscribir_en_curso(curso_poo)

    estudiante_juan.inscribir_en_curso(curso_calculo)
    estudiante_juan.inscribir_en_curso(curso_fisica)

    estudiante_clara.inscribir_en_curso(curso_poo)

    estudiante_pedro.inscribir_en_curso(curso_fisica)
    estudiante_pedro.inscribir_en_curso(curso_poo)

    print("\n" + "="*40)
    print("--- Reporte Final de Inscripciones ---")
    print("="*40)

    # c) Imprimir los cursos a los que está inscrito cada estudiante
    print("\n--- Cursos por Estudiante ---")
    todos_los_estudiantes = [estudiante_ana, estudiante_juan, estudiante_clara, estudiante_pedro]
    for estudiante in todos_los_estudiantes:
        nombres_cursos = [curso.nombre for curso in estudiante.cursos_inscritos]
        print(f"{estudiante.nombre} está inscrito/a en: {', '.join(nombres_cursos)}")

    # c) Imprimir los nombres de los estudiantes inscritos en cada curso
    print("\n--- Estudiantes por Curso ---")
    todos_los_cursos = [curso_calculo, curso_fisica, curso_poo]
    for curso in todos_los_cursos:
        nombres_estudiantes = [estudiante.nombre for estudiante in curso.estudiantes_inscritos]
        print(f"{curso.nombre} tiene los siguientes inscritos: {', '.join(nombres_estudiantes)}")