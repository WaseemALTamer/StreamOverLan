import socket
import display
import time
import threading
import statistics

photo = b""

def window():
    global data
    while True:
        try:
            display.display(photo)
        except:
            pass
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 1234)
sock.bind(server_address)
sock.settimeout(2)

timer = time.time()
fps = 0

threading.Thread(target=window).start()
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
                print(fps)
                fps = 0
            try:
                data = client_sock.recv(455000)
                checker.append(data[-1])
                if len(checker) == 0:
                    checker = checker[1:]

                if data[-1] == statistics.mode(checker):
                    #display.display(data)
                    photo = data
                    pass
                fps += 1
            except socket.timeout:
                display.close()
                pass
    except socket.error as e:
        display.close()
        print('Error occurred:', e)