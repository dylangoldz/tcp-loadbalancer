# TCP Load Balancer

This project implements a simple TCP load balancer using Python and Docker. It distributes incoming requests to multiple backend servers using a round-robin algorithm.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:

2. Build and start the Docker containers:
   ```bash
   cd docker
   docker-compose up --build
   ```

## Usage

- The load balancer listens on port `8080` and forwards requests to backend servers on ports `9001`, `9002`, and `9003`.
- You can test the load balancer by sending requests using `curl`:
  ```bash
  curl http://localhost:8080
  ```
- The load balancer will distribute requests across the backend servers in a round-robin fashion.

## Features
- Round-robin load balancing
- Dockerized setup for easy deployment
- Real-time logging with immediate flush

## Potential Improvements
- Implement health checks for backend servers
- Add support for different load balancing algorithms
- Integrate metrics and monitoring tools
- Enable SSL/TLS termination
- Add rate limiting and connection pooling
- Develop an admin interface for monitoring and configuration

## Overview

This project is an L4 TCP load balancer that distributes incoming client requests to a pool of backend servers using a round-robin approach. The load balancer ensures that client requests are evenly distributed across the available backend servers, providing efficient load distribution and improved performance.

## Features

- **Layer 4 Load Balancing**: Operates at the transport layer (TCP), forwarding client requests to backend servers.
- **Round-Robin Distribution**: Uses a round-robin algorithm to distribute client requests evenly across backend servers.
- **Concurrency**: Handles multiple client connections concurrently using threading.
- **Logging**: Logs client requests and backend server connections for monitoring and debugging.

## How It Works

1. **Initialization**: The load balancer initializes a list of backend servers and sets up a listening socket to accept incoming client connections.
2. **Round-Robin Algorithm**: The load balancer maintains a round-robin index to keep track of the next backend server to forward the client request to.
3. **Client Handling**: When a client connects, the load balancer selects the next backend server using the round-robin algorithm and establishes a connection.
4. **Data Forwarding**: The load balancer forwards data between the client and the selected backend server, ensuring seamless communication.
5. **Concurrency**: Each client connection is handled in a separate thread, allowing the load balancer to manage multiple connections simultaneously.

## Usage

To start the load balancer, run the `main.py` script:

```sh
python [main.py](http://_vscodecontentref_/0)
