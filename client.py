import sys
import socket
import threading


try:
    host = sys.argv[1]
    port = int(sys.argv[2])

    alias = input('Choose an alias >>> ')
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, port))

    def client_receive():
        while True:
            try:
                msg = client.recv(1024).decode('utf-8')
                if msg == 'alias?':
                    client.send(alias.encode('utf-8'))
                else:
                    print(msg)
            except:
                print('Error!')
                client.close()
                break

        

    def client_send():
        while True:
            msg = f'{alias}. {input("")}'
            client.send(msg.encode('utf-8'))
            
    receive_thread = threading.Thread(target= client_receive)
    receive_thread.start()

    send_thread = threading.Thread(target= client_send)
    send_thread.start()


except ValueError:
    print('Please use a integer as input')

# except (IndexError, TypeError):
#     print('Usage:')
#     print('python3 client.py [ip address] [port number] ')
    
