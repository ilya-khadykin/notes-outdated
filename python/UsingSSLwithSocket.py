import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
secure_sock = ssl.wrap_socket(s)

try:
    secure_sock.connect(('www.google.com', 443))  # HTTPS
    print(secure_sock.cipher())
except Exception as e:
    print('Error: ', e)

try:
    secure_sock.write(b'GET / HTTP/1.1 \r\n')
    secure_sock.write(b'Host: www.google.com\n\n')
except Exception as e:
    print('Socket Write error: ', e)

data = bytearray()
try:
    data = secure_sock.read()
except Exception as e:
    print('Socket Read error: ', e)

s.close()
secure_sock.close()
print(data.decode('utf-8'))