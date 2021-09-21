import socket

hostname = str(input('Please input any website URL: '))
try:
    print(f'Hostname: {hostname}')
    print(f'IP: {socket.gethostbyname(hostname)}')
except socket.gaierror as error:
    print(f'Invalid URL, error throw: {error}')
