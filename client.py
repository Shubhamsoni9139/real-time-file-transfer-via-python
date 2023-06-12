import socket
import os
def client_program():
 host = '127.0.0.1'
 port = 8888
 client_socket = socket.socket()
 client_socket.connect((host, port))
 while True:
 print("\nWelcome to the client program!")
 print("Menu:")
 print("1. Send a file")
 print("2. Open chat system")
 print("3. Send an image")
 print("4. Close the program")
 choice = input("Enter your choice (1, 2, 3, or 4): ")
 if choice == '1':
 send_file(client_socket)
 elif choice == '2':
 open_chat_system(client_socket)
 elif choice == '3':
 send_image(client_socket)
 elif choice == '4':
 print("Closing the program...")
 print("Program CLosed Successfully")
 break
 else:
 print("Invalid choice. Please try again.")
 client_socket.close()
def open_chat_system(connection):
 print("Chat system opened.")
 print("You can start chatting with the server.")
 print("Type 'bye' to exit the chat system.")
 while True:
 message = input("-> ")
 if message.lower().strip() == 'bye':
 connection.send(message.encode())
 break
 connection.send(message.encode())
 data = connection.recv(1024).decode()
 print('Received from server: ' + data)
def send_file(connection):
 filepath = input("Enter the file path: ")
 filename = os.path.basename(filepath)
 if not os.path.exists(filepath):
 print(f"File '{filename}' does not exist.")
 return
 connection.send('file'.encode())
 connection.recv(1024) # Wait for the server to respond with 'Ready to receive file'
 connection.send(filename.encode())
 with open(filepath, 'rb') as file:
 data = file.read(1024)
 while data:
 connection.send(data)
 data = file.read(1024)
 print(f"File '{filename}' sent successfully.")
def send_image(connection):
 filepath = input("Enter the image path: ")
 filename = os.path.basename(filepath)
 if not os.path.exists(filepath):
 print(f"Image '{filename}' does not exist.")
 return
 connection.send('image'.encode())
 connection.recv(1024) # Wait for the server to respond with 'Ready to receive image'
 connection.send(filename.encode())
 with open(filepath, 'rb') as file:
 data = file.read(1024)
 while data:
 connection.send(data)
 data = file.read(1024)
 print(f"Image '{filename}' sent successfully.")
if __name__ == '__main__':
 client_program()
