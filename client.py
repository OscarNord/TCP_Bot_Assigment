from posixpath import split
import sys
import socket
import threading
import os
from tkinter import E


try:
    
    host = sys.argv[1]  #Takes ip as first argument
    port = int(sys.argv[2]) #Takes port as second argument

    
    name = input('Pick a name >>> ')
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #Creates socket with ipv4 and 
    client.connect((host, port))
    

    # function that handles servers connection
    def client_receive():
        while True:
            try:
                msg = client.recv(1024).decode('utf-8')
                if msg == 'shutdown':
                    print("Lost connection to server")
                    client.close()
                    break
                if msg == 'name?':
                    client.send(name.encode('utf-8'))
                else:
                    print(msg)
                    if msg == 'Have a nice day!':
                        client.close() 
                        break
                        
            except:
                print('Something went wrong!')
                client.close()
                break

        os._exit(1)


    # function that sends messages to server
    def client_send():
        while True:
            msg = f'[{name}]: {input("")}'
            client.send(msg.encode('utf-8'))


    # main function that starts threads
    def main():
        receive_thread = threading.Thread(target= client_receive)
        send_thread = threading.Thread(target= client_send)
        receive_thread.start()
        send_thread.start()
        receive_thread.join()
        send_thread.join()


    if __name__ == "__main__":
        main()


# Handles exceptions that may rise
except ValueError:
    print('Please use a integer as input')

except (IndexError, TypeError):
    print('Usage:')
    print('python3 client.py [ip address] [port number] ')

except KeyboardInterrupt:
    print("\nClient shutted down")
    os._exit(1)

except ConnectionRefusedError:
    print("\nServer is not up and running on this port")
