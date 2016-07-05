import socket
import re

connect_addr = input('Input name of the website you want to check: ')

connection_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # SOCK_STREAM == TCP
connection_socket.connect((connect_addr, 80))  # connecting to a remote host's web server on port 80

request_bytesstr = b'GET / HTTP/1.1\nHost: ' + bytes(connect_addr, 'utf-8') + b'\n\n'

response_data = ''
try:
    print('Connecting to: ', connect_addr)
    connection_socket.sendall(request_bytesstr)
    response_data = connection_socket.recvfrom(1024)
except socket.errno:
    print('Socket Error: ', socket.errno)
finally:
    print('Closing connection...')
    connection_socket.close()

str_response_data = response_data[0].decode('utf-8')
# splitting one long line to a list of strings
headers = str_response_data.splitlines()
# use regular expression to find to look for the info we want to extract
for s in headers:
    if re.search('Server:', s):
        s = s.replace('Server: ', '')
        print('\n' + connect_addr + ' (' + socket.gethostbyname(connect_addr) + ')' + ' is running with ' + s)