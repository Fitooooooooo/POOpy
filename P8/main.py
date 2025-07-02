"""
Este módulo simula un sistema de mensajería entre usuarios, donde cada
usuario puede enviar y recibir mensajes.
"""
from __future__ import annotations

class Usuario:
    """
    Representa un usuario en el sistema de mensajería.

    Atributos:
        nombre (str): El nombre del usuario.
        buzon (list[dict]): Una lista de diccionarios, donde cada uno
                            representa un mensaje recibido.
    """
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo usuario.

        Args:
            nombre: El nombre del usuario.
        """
        self.nombre = nombre
        self.buzon: list[dict] = []

    def enviar_mensaje(self, destinatario: Usuario, contenido: str):
        """
        Envía un mensaje a otro usuario.

        Args:
            destinatario: El objeto Usuario que recibirá el mensaje.
            contenido: El texto del mensaje a enviar.
        """
        mensaje = {
            "remitente": self.nombre,
            "contenido": contenido
        }
        # El objeto 'destinatario' recibe el mensaje en su propio buzón.
        destinatario.buzon.append(mensaje)
        print(f"Info: Mensaje de '{self.nombre}' enviado a '{destinatario.nombre}'.")

    def leer_mensajes(self) -> list[str]:
        """
        Devuelve una lista formateada de todos los mensajes en el buzón.

        Returns:
            Una lista de strings, cada uno representando un mensaje.
        """
        mensajes_formateados = []
        for mensaje in self.buzon:
            texto = f"De: {mensaje['remitente']} - '{mensaje['contenido']}'"
            mensajes_formateados.append(texto)
        return mensajes_formateados


# --- Sección de Simulación---
if __name__ == "__main__":
    print("--- Sistema de Mensajería ---")

    # Crear usuarios
    u1 = Usuario("Alicia")
    u2 = Usuario("Juan")
    u3 = Usuario("Clara")

    # Simular envío de mensajes
    print("\nEnviando mensajes...")
    u1.enviar_mensaje(u2, "Hola Juan, ¿cómo estás?")
    u2.enviar_mensaje(u1, "Hola Alicia, todo bien. ¿Y tú?")
    u3.enviar_mensaje(u1, "Alicia, ¿tienes un momento?")
    u1.enviar_mensaje(u3, "Claro Clara, dime.")

    # Leer los mensajes de cada usuario
    print("\n--- Revisando Buzones ---")
    print("Mensajes de Alicia:", u1.leer_mensajes())
    print("Mensajes de Juan:", u2.leer_mensajes())
    print("Mensajes de Clara:", u3.leer_mensajes())