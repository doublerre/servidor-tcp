import socket

HOST = 'localhost'
PORT = 5000  

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor {HOST}:{PORT}")

        while True:
            message = input("Escribe un mensaje (o escribe 'DESCONEXION') para salir: ")
            client_socket.sendall(message.encode('utf-8'))

            if message == "DESCONEXION":
                print("Desconectando del servidor...")
                break

            response = client_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    start_client()