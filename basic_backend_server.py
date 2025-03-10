import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9001  # Allow port selection

def start_backend_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, port))
    server_socket.listen(5)
    print(f"Backend Server running on {HOST}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Server-{port}: Connection from {addr}")

        try:
            data = client_socket.recv(4096)  # Receive request
            if data:
                response_body = f"Hello from Backend {port}"  # Identify backend

                # Send a proper HTTP response
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "\r\n"
                    f"{response_body}"
                )
                client_socket.sendall(response.encode())

        except Exception as e:
            print(f"Server-{port}: Error: {e}")

        finally:
            client_socket.shutdown(socket.SHUT_RDWR)

if __name__ == "__main__":
    start_backend_server(PORT)
