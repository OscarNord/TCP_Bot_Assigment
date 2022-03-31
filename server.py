import threading
import sys
import socket
from bots import *
import os


clients = []    # list over connectins to server
names = []  # list over names of connections
try:     

    # function forwards message sent from SENDER to all the other clients
    def broadcast(msg: str, SENDER = None):
        for client in clients:
            if SENDER != client:    #Skips SENDER
                client.send(f'{msg}'.encode('utf-8'))
      
    # Funtion to handle clients' connections
    def handle_client(client):
        while True:
            try:
                msg = client.recv(1024).decode('utf-8')
                broadcast(msg, client)
                if msg.split()[-1] == 'farewell':   # If message is farewell...
                    client.send("Have a nice day!".encode('utf-8')) 
                    break   #... then we close their connection with the server

                broadcast(bot(msg))
            except:
                break

        client_leave(client) #cuts connetion at the end


    # funtion that cuts clients connection with server
    def client_leave(leavingClient):
            index = clients.index(leavingClient)
            clients.remove(leavingClient)
            leavingClient.close()
            name = names[index]
            print(f'{name} disconnected from server.')
            broadcast(f'{name} has left the chat room!')
            names.remove(name)
    


    # Main function to receive the clients connection
    def receive():
        host = sys.argv[1]  #Gets ip address from first argument
        port = int(sys.argv[2]) #Gets port from second argument
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Creats socket
        print("Socket is now created")
        sock.bind((host, port)) #Binds host and port
        sock.listen()       #Listens after connections
        
        #loop that accepts incoming clients and connect them to server
        while True:
            print('Server is listening for connections...')
            client, address = sock.accept()     #accepts incoming connections
            print(f'New client connected: {str(address)}')
            client.send('name?'.encode('utf-8'))
            name = client.recv(1024).decode('utf-8')
            names.append(name)  #stores name of client
            clients.append(client)  #stores client
            broadcast(f'{name} has connected to the chat room!')
            client.send('\nWelcome to the chat room!\n'.encode('utf-8'))
            client.send('\nIf you wish to leave, write "farewell"\n'.encode('utf-8'))
            if len(clients) <= 1:   #Checks if the connected client is the alone when entering
                client.send("\nWhat do you like to do?".encode('utf-8'))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
         

    if __name__ == "__main__":
        receive()


#Handles different errors that may occur
except ValueError:
    print('Please use a integer as input')
    print('Usage:')
    print('python3 server.py [ip address] [port number] ')

except IndexError as indx:
    print(indx)
    print('Usage:')
    print('python3 server.py [ip address] [port number] ')

except TypeError as typ:
    print(typ)
    print('Something went wrong!')
    for client in clients:
        client.send("shutdown".encode('utf-8'))
    os._exit(1)
    
except KeyboardInterrupt:
    for client in clients:
        client.send("shutdown".encode('utf-8'))
    print("\nClosing server...")
    os._exit(1)