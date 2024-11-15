# Ejercicio de Servidor y Cliente TCP

Este proyecto contiene un servidor y un cliente TCP en Python que pueden comunicarse entre sí en la misma máquina (localhost) usando el puerto 5000.

## Versión de python utilizada
- Python v3.13.0

## Instrucciones para ejecutar el servidor y el cliente

1. Clona el repositorio o descarga los archivos `tcp_server.py` y `tcp_client.py`.
2. Abre dos terminales:
   - En la primera terminal, inicia el servidor:
     ```bash
     python tcp_server.py
     ```
   - En la segunda terminal, inicia el cliente:
     ```bash
     python tcp_client.py
     ```

3. En el cliente, escribe mensajes y presiona Enter para enviarlos al servidor.
   - El servidor responderá con el mensaje en mayúsculas.
   - Si ingresas "DESCONEXION", la conexión se cerrará y el programa cliente terminará.

## Pruebas Manuales

1. **Prueba de mensaje de texto normal**:
   - Envía un mensaje al servidor (ej. "hola servidor").
   - El servidor debe responder con el mensaje en mayúsculas ("HOLA SERVIDOR").

2. **Prueba de desconexión**:
   - Envía el mensaje "DESCONEXION".
   - El cliente debe desconectarse y cerrar el programa.
   - El servidor debe seguir disponible para aceptar nuevos clientes.

## Ejemplo de interacción

```plaintext
Cliente:
Escribe un mensaje (o 'DESCONEXION' para salir): hola servidor
Respuesta del servidor: HOLA CLIENTE

Cliente:
Escribe un mensaje (o 'DESCONEXION' para salir): DESCONEXION
Desconectando del servidor...