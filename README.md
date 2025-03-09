# tcp-loadbalancer# TCP Load Balancer

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