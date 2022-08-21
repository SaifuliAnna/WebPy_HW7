import socket


def client():
    host = socket.gethostname()
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = host, port
        sock.connect(server)
        print(f'Connection established {server}')

        message = input('---> ')

        while message.lower().strip() != "end":
            for line in message.split(' '):
                print(f'Send message: {line}')
                sock.send(line.encode())
                response = sock.recv(1024).decode()
                print(f'Response message: {response}')
                message = input('---> ')

        sock.close()

    print(f'Data transfer completed')


if __name__ == "__main__":
    client()
