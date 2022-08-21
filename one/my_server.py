import socket


def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f'received message: {data}')
        data = input('---> ')
        conn.send(data.encode())
    conn.close()


if __name__ == "__main__":
    main()
