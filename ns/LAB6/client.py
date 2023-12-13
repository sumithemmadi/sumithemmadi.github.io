import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

client_socket.sendall("REQUEST_PARAMS".encode('utf-8'))
response = client_socket.recv(1024).decode('utf-8')

if response == "SEND_PARAMS":
    params = client_socket.recv(1024).decode('utf-8')
    prime, base = map(int, params.split(','))

    print("Received prime:", prime)
    print("Received base:", base)

    client_private_key = int(input("Enter Y value: "))
    client_public_key = (pow(base, client_private_key) % prime)

    client_socket.sendall(str(client_public_key).encode('utf-8'))

    server_public_key = int(client_socket.recv(1024).decode('utf-8'))
    print("server_public_key:", server_public_key)

    shared_secret = pow(server_public_key, client_private_key, prime)
    print("secret key:", shared_secret)

client_socket.close()
