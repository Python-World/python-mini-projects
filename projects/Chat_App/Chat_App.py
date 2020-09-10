# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:51:16 2019

@author: Ajayi Raymond T
"""
'''server for multithread (asynchronous) chat application'''
from socket import AF_INET, socket, SOCK_STREAM
from threading import thread

def acc_inc_conn():
    'sets uphandling for incoming calls.'
    while True:
        clients, client_address = SERVER.accept()
        print('%s:%s has connected.' % client_address)
        client.send(bytes('Greetings from the cave! Now type your name'))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
        
def handle_client(client):#Takes client socket as argument.
    '''handles a single client connection'''
    name = client.recv(BUFSIZ).decode('utf8')
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to '
    msg = '$s has joined the chat!'% name
    broadcast(bytes(msg,'utf8'))
    clients[client] = name
    
    while True:
        msg = client.recv(BUZFIZ)
        if msg != bytes('{quit}','utf8'):
            broadcast(msg,name+':')
        else:
            client.send(bytes('{quit}','utf8'))
            client.close()
            