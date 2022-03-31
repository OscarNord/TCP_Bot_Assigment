from posixpath import split
import sys
import socket
import threading
import os

notRunning = False
try:
    host = sys.argv[1]
    port = int(sys.argv[2])

    name = input('Choose a name >>> ')
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, port))
    
    
    
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
                print('Error!')
                client.close()
                break
     
        os._exit(1)


    def client_send():
        while True:
            msg = f'[{name}]: {input("")}'
            client.send(msg.encode('utf-8'))

    
    receive_thread = threading.Thread(target= client_receive)
    receive_thread.start()

    send_thread = threading.Thread(target= client_send)
    send_thread.start()
    receive_thread.join()
    send_thread.join()

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
