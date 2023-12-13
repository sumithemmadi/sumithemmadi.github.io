import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server listening on port 8080...")

while True:
    connection, client_address = server_socket.accept()
    print("Connection from", client_address)

    connection.sendall("SEND_PARAMS".encode('utf-8'))
    request = connection.recv(1024).decode('utf-8')

    if request == "REQUEST_PARAMS":
        base = 5
        prime = 23

        connection.sendall(f"{prime},{base}".encode('utf-8'))

        server_private_key = int(input("Enter Y value: "))
        server_public_key = (pow(base, server_private_key) % prime)

        client_public_key = int(connection.recv(1024).decode('utf-8'))

        print("client_public_key :", client_public_key)

        shared_secret = pow(client_public_key, server_private_key, prime)
        print("secret key :", shared_secret)

        connection.sendall(str(server_public_key).encode('utf-8'))

        connection.close()
