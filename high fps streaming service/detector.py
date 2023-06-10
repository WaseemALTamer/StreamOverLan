import socket
import display
import time
import threading
import statistics
import pygame
import pydisolay

photo = b""

def window():
    global data, timer

    while True:
        #if time.time() > timer:
            #timer = time.time() + 1
            #print(fps)
        try:
            pydisolay.run(photo)
            pygame.time.wait(3)
        except:
            pass

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 1234)
sock.bind(server_address)
sock.settimeout(2)

timer = time.time()
fps = 0

#threading.Thread(target=window).start()
threading.Thread(target=window).start()

checker = []

while True:
    try:
        sock.listen(1)
        print('Waiting for a client connection...')
        client_sock, client_address = sock.accept()
        print('Accepted connection from', client_address)
        while True:
            if time.time() > timer:
                timer = time.time() + 1
                #print(fps)
                fps = 0
            try:
                data = client_sock.recv(455000)
                checker.append(data[-1])
                if len(checker) == 5:
                    checker = checker[1:]
                if data[-1] == statistics.mode(checker):
                    #pydisolay.run(data)
                    photo = data
                    pass
                fps += 1
            except socket.timeout:
                pass
    except socket.error as e:
        print('Error occurred:', e)