# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:44:11 2019

@author: Ajayi Raymond T
"""

from socket import AF_INET,socket, SOCK_STREAM
from threading import Thread
import tkinter
my_msg = ''

def receive():
    '''handles receiving messages'''
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode('utf8')
            msg_list.insert(tkinter.END,msg)
        except OSError:#possibly client has left the chat
            break
        
def send(event=None):#event is passe dby binders'
    global my_msg
    '''Handles sending of messages.'''
    msg = my_msg.get()
    my_msg.set('')#clears input field
    client_socket.send(bytes(msg, 'utf8'))
    if msg == '{quit}':
        client_socket.close()
        top.quit()
        
def on_closing(event=None):
    global my_msg
    '''this func is to be called when the window is closed'''
    my_msg.set('{quit}')
    send()
top = tkinter.Tk()
top.title('Chatter')

messages_frame = tkinter.Frame(top,bg='green')
my_msg = tkinter.StringVar() # for the msgs to be sent
my_msg.set(' Type your Identity here:')
scrollbar = tkinter.Scrollbar(messages_frame) #to navigate through past msgs
#following will contain the messages
msg_list = tkinter.Listbox(messages_frame,bg ='light green', height =15,width=50,yscrollcommand= scrollbar.set)
scrollbar.pack(side = tkinter.LEFT,fill =tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top,textvariable= my_msg)
entry_field.bind('<Return>',send)
entry_field.pack()
send_button = tkinter.Button(top , text = 'send',bg='navy blue',fg='cyan', command =send)
send_button.pack()

top.protocol('WM_DELETE_WINDOW',on_closing)
#-----Now comes the socket part---------
HOST = input ('Enter Host:')
PORT = input ('Enter Port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int (PORT)
BUFSIZ = 1024
ADDR = (HOST,PORT)

client_socket = socket (AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() # starts GUI excecution

    
    