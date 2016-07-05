import socket

SIZE = 512
HOST = ''
PORT = 8000


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    conn, addr = server_socket.accept()
    data = conn.recv(SIZE)
    if data:
        print('Connection from: ' +  str(addr[0]) + ':' + str(addr[1]))
        print(data.decode('utf-8'))
    server_socket.close()

if __name__ == '__main__':
    main()