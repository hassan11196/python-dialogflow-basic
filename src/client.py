
import socket

HOST = '127.0.0.1'  

PORT = 1999        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Ask me Questions')
    while True:
        
        question = input('Text to send: ')
        s.sendall(str.encode(question))
        data = s.recv(1024)
        print('Text from Server : ', str(data))
