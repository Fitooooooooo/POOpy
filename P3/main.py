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
        """Permite al estudiante inscribirse en un curso."""
        # Por ahora, solo cumple el requisito de agregar el curso a la lista del estudiante.
        self.cursos_inscritos.append(curso)