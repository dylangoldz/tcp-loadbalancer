import socket
import threading
import sys

# List of backend servers (IP, Port)
BACKEND_SERVERS = [
    ("backend1", 9001),
    ("backend2", 9002),
    ("backend3", 9003)
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
        print(f"Handling client request from {client_socket.getpeername()} to backend {backend_ip}:{backend_port}", flush=True)
        
        # Connect to the backend server
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Attempting to connect to backend {backend_ip}:{backend_port}", flush=True)
        backend_socket.connect((backend_ip, backend_port))
        print(f"Successfully connected to backend {backend_ip}:{backend_port}", flush=True)
        
        # Forward data between client and backend server
        client_thread = threading.Thread(target=forward_data, args=(client_socket, backend_socket, "client->backend"))
        backend_thread = threading.Thread(target=forward_data, args=(backend_socket, client_socket, "backend->client"))
        
        client_thread.start()
        backend_thread.start()
        
        client_thread.join()
        backend_thread.join()

    except Exception as e:
        print(f"Error connecting to backend {backend_ip}:{backend_port} - {e}", flush=True)
    finally:
        print(f"Closing connection to backend {backend_ip}:{backend_port}", flush=True)
        client_socket.close()
        backend_socket.close()
    

def forward_data(source, destination, direction):
    """Forwards data between two sockets."""
    try:
        while True:
            data = source.recv(4096)
            if not data:
                print(f"{direction}: Connection closed by peer", flush=True)
                break
            print(f"{direction}: Forwarding {len(data)} bytes", flush=True)
            destination.sendall(data)
            # If this is a response from backend to client, we need to ensure all data is sent
            if direction == "backend->client":
                break
    except Exception as e:
        print(f"{direction}: Error forwarding data - {e}", flush=True)

def start_load_balancer(host="0.0.0.0", port=8080):
    print("Starting Load Balancer", flush=True)
    """Starts the L4 load balancer."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(100)
    print(f"L4 Load Balancer listening on {host}:{port}", flush=True)
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}", flush=True)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    # Force stdout to be line-buffered
    sys.stdout.reconfigure(line_buffering=True)
    start_load_balancer()
