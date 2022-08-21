import socket
from concurrent import futures as cf


def main():
    host = socket.gethostname()
    port = 5000

    def handle(sock: socket.socket, address: str):
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024).decode()
            if not received:
                break
            print(f'Data received: {received}')
            received = input('---> ')
            sock.send(received.encode())
        print(f'Socket connection closed {address}')
        sock.close()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(3)
    print(f'Start echo server {server_socket.getsockname()}')
    with cf.ThreadPoolExecutor(3) as client_pool:
        try:
            while True:
                conn, address = server_socket.accept()
                client_pool.submit(handle, conn, address)
        except KeyboardInterrupt:
            print(f'Destroy server')
        finally:
            server_socket.close()


if __name__ == "__main__":
    main()
