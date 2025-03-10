import socket
import threading

# List of backend servers (IP, Port)
BACKEND_SERVERS = [
    ("127.0.0.1", 9001),
    ("127.0.0.1", 9002),
    ("127.0.0.1", 9003)
]

# Round-robin index
current_server = 0
lock = threading.Lock()

def get_next_server():
    global current_server
    with lock:
        server = BACKEND_SERVERS[current_server]
        current_server = (current_server + 1) % len(BACKEND_SERVERS)
    return server

def handle_client(client_socket):
    backend_ip, backend_port = get_next_server()
    
    try:
        # Log client request
        print(f"Handling client request from {client_socket.getpeername()} to backend {backend_ip}:{backend_port}")
        
        # Connect to the backend server
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((backend_ip, backend_port))
        
        # Forward data between client and backend server
        client_thread = threading.Thread(target=forward_data, args=(client_socket, backend_socket))
        backend_thread = threading.Thread(target=forward_data, args=(backend_socket, client_socket))
        
        client_thread.start()
        backend_thread.start()
        
        client_thread.join()
        backend_thread.join()

    except Exception as e:
        print(f"Error connecting to backend {backend_ip}:{backend_port} - {e}")
    finally:
        client_socket.close()
        backend_socket.close()
    

def forward_data(source, destination):
    """Forwards data between two sockets."""
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.sendall(data)
    except Exception as e:
        print(f"Connection closed: {e}")

def start_load_balancer(host="0.0.0.0", port=8080):
    """Starts the L4 load balancer."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(100)
    print(f"L4 Load Balancer listening on {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_load_balancer()
