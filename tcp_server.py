import socket

HOST = 'localhost'
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor iniciado en {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Conexión establecida con {client_address}")

            with client_socket:
                while True:
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:
                        break
                    print(f"Mensaje recibido: {message}")

                    if message == "DESCONEXION":
                        print("Cerrando conexión con el cliente.")
                        break

                    if message == "hola servidor":
                        response = "HOLA CLIENTE"
                        client_socket.sendall(response.encode('utf-8'))
                    else:
                        response = message.upper()
                        client_socket.sendall(response.encode('utf-8'))
            print("Esperando nueva conexión")

if __name__ == "__main__":
    start_server()