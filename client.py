import socket
import sys
# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 10000)

try:
    client.connect(server_address)
    print("Connected to server at", server_address)

    # Get the message from the user
    message = input("Enter your message: ")

    client.sendall(message.encode())  

    while message.lower() != 'end':
    
        data = client.recv(1000).decode()
        if data:
            print("Received from server:", data)
            message = input("Enter your message: ")
            client.sendall(message.encode())  
        else:
            print("No data received. Closing connection.")
            break

finally:
    client.close()  
    print("Connection closed.")
