# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:51:16 2019

@author: Ajayi Raymond T
"""
'''server for multithread (asynchronous) chat application'''
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def acc_inc_conn():
    'sets uphandling for incoming calls.'
    while True:
        client, client_address = SERVER.accept()
        print('%s:%s has connected.' % client_address)
        client.send(bytes('Greetings from the cave! Now type your name and press enter!', 'utf8'))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
        
def handle_client(client):#Takes client socket as argument.
    '''handles a single client connection'''
    name = client.recv(BUFSIZ).decode('utf8')
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome,'utf8'))
    msg = '%s has joined the chat!'% name
    broadcast(bytes(msg,'utf8'))
    clients[client] = name
    
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes('{quit}','utf8'):
            broadcast(msg,name+':')
        else:
            client.send(bytes('{quit}','utf8'))
            client.close()
            del clients[client]
            broadcast(bytes('%s has left the chat.' % name, 'utf8'))
            break
        
def broadcast(msg,prefix=''):#prefix is for name identification.
    '''Broadcast a message to all the clientss.'''
    for sock in clients:
        sock.send(bytes(prefix,'utf8')+msg)
        
clients = {}
addresses = {}

HOST= ''
PORT= 33000
BUFSIZ = 1024
ADDR = (HOST,PORT)

SERVER = socket (AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == '__main__':
    SERVER.listen(5)
    print('Waiting for connection...')
    ACCEPT_THREAD = Thread(target=acc_inc_conn)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()            