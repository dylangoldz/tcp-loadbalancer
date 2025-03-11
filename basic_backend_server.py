import socket
import os
import sys

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = int(os.getenv("PORT", 9001))  # Allow port selection

def start_backend_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, port))
    server_socket.listen(5)
    print(f"Backend Server running on {HOST}:{port}", flush=True)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Server-{port}: Connection from {addr}", flush=True)

        try:
            data = client_socket.recv(4096)  # Receive request
            print(f"Server-{port}: Received {len(data)} bytes", flush=True)
            if data:
                response_body = f"Hello from Backend {port}"  # Identify backend
                print(f"Server-{port}: Sending response", flush=True)

                # Send a proper HTTP response
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "\r\n"
                    f"{response_body}"
                )
                client_socket.sendall(response.encode())
                print(f"Server-{port}: Response sent successfully", flush=True)

        except Exception as e:
            print(f"Server-{port}: Error: {e}", flush=True)

        finally:
            try:
                print(f"Server-{port}: Closing connection", flush=True)
                client_socket.close()
            except:
                pass

if __name__ == "__main__":
    # Force stdout to be line-buffered
    sys.stdout.reconfigure(line_buffering=True)
    start_backend_server(PORT)
