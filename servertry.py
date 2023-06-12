import socket

def server_program():
    host = '172.16.145.150'
    port = 8888

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))

        # Check if the user wants to send a file
        if data.lower() == 'file':
            conn.send('Ready to receive file'.encode())
            receive_file(conn)

        # Check if the user wants to send an image
        elif data.lower() == 'image':
            conn.send('Ready to receive image'.encode())
            receive_image(conn)

        else:
            data = input(' -> ')
            conn.send(data.encode())

    conn.close()

def receive_file(connection):
    filename = connection.recv(1024).decode()
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"File '{filename}' received successfully.")

def receive_image(connection):
    filename = connection.recv(1024).decode()
    with open(filename, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"Image '{filename}' received successfully.")

if __name__ == '__main__':
    server_program()
