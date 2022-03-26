import threading
import sys
import socket


try: 
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket created")
    sock.bind((host, port))

    sock.listen()
    print("Waiting for connections")
    clients = []
    aliases = []

    def broadcast(msg):
        for client in clients:
            client.send(msg)

    # Funtion to handle clients' connections
    def handle_client(client):
        while True:
            try:
                msg = client.recv(1024)
                # Send msg videre til bot som returnerer svar


                broadcast(msg)
            except:
                index = clients.index(client)
                client.remove(client)
                client.close()
                alias = aliases[index]
                broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
                aliases.remove(alias)
                break

    # Main function to receive the clients connection

    def receive():
        while True:
            print('Server is running and listening ...')
            client, address = sock.accept()
            print(f'connection is established with {str(address)}')
            client.send('alias?'.encode('utf-8'))
            alias = client.recv(1024)
            aliases.append(alias)
            clients.append(client)
            print(f'The alias of this client is {alias}'.encode('utf-8'))
            broadcast(f'{alias} has connected to the chat room!'.encode('utf-8'))
            client.send('you are now connected!'.encode('utf-8'))
            thread = threading.Thread(target= handle_client, args=(client,))
            thread.start()

    if __name__ == "__main__":
        receive()
except ValueError:
    print('Please use a integer as input')

except IndexError as indx:
    print(indx)
    print('Usage:')
    print('python3 server.py [ip address] [port number] ')
    