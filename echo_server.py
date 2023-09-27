#!/usr/bin/env python3
import socket
import time
from threading import Thread

#define address & buffer size
HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024
BYTES_TO_READ = 4096

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        conn, addr = s.accept()
        
        #recieve data, wait a bit, then send it back
        handle_connection(conn, addr)

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while True:
            conn, addr = s.accept()
            thread = Thread()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

if __name__ == "__main__":
    start_threaded_server()
