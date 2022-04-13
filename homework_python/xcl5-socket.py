from collections import UserString
import socket,threading
from pprint import print 

HOST = '127.0.0.1'
PORT = 12345

def enc(s):
    return s.encode('utf-8')

def dec(s):
    return s.decode('utf-8')

def server_auth(user):
    while True:
        user.send(enc('Type your name: '))
        username = dec(user.recv(1024))
        if username not in users.keys():
            print('User {0[0]} : {0[1]} connected as {1}'\
                .format(address, username))
            
            print('\nNow connected: \n')
            pprint(users)
            user.send(enc('Auth ok'))
            return username

def new_client(client_socket, username):
    global users
    while True:
        
if __name__=='_main_': #проверяем, основная ли программа 
    server_socket = socket.socket()

    server_socket.bind((HOST, PORT)) #socket закреплён за опред. адресом
    server_socket.listen() #слушаем адрес, ждём соединение

    users = dict() #addrs

try:
    user, address = server_socket.accept() #принимает подключениие, возвращ. 2 сущности (user + адрес), связывается с клиентом
    print('Connected: ', address) #запуск только после accept
    
    while True:
        msg = input('\ntype your msg: ')
        if msg == 'q':
            break
        user.send(msg.encode('utf-8')) #отправка пользователю сообщение, кодирование строки
        recv_msg = user.recv(1024)
        print('\nIncoming msg:\n')
        print(recv_msg.decode('utf-8')) 

except KeyboardInterrupt:   
    print('\nserver shut down') 
    server_socket.close() 

except Exception as e:
    print(e)
    server_socket.close() 

server_socket.close() #закрытие соединения 



#from http import client
import socket 
#from server import HOST, PORT, enc, dec

client_socket = socket.socket()
client_socket.connect((HOST, PORT)) #соединение

#получение сообщения от сервера (receiv)

#try:
    #msg = client_socket.recv(1024) #receive (сообщение от сервера), макс. кол-во байтов, которое хотим принять
    #print(msg.decode('utf-8')) #декодирование сообщения от сервера
try:
    recv_msg = client_socket.recv(1024) 
    print('\nIncomming msg:\n')
    print(dec(recv_msg)) #декодир-е сообщения от сервера
        
    while True:
        msg = input('\nType msg: ')
        client_socket.send(enc(msg))
        if msg == 'q':
            break 

        # recv_msg = client_socket.recv(1024)
        # msg = client_socket.recv(1024) 
        # print('\nIncomming msg:\n')
        # print(recv_msg.decode('utf-8')) #декодир-е сообщения от сервера
        # msg = input('\nType msg: ')
        # if msg == 'q':
        #     client_socket.send('q'.encode('utf-8'))
        #     break
        # client_socket.send(msg.encode('utf-8')) #отправка сообщения на сервер

except KeyboardInterrupt:
    print('\nserver shut down')
    client_socket.send(enc('q'))
    client_socket.close()

except Exception as e:
    print(e)
    client_socket.close() 

client_socket.close()

