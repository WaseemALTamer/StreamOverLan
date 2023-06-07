import socket
import display
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 1234)
sock.bind(server_address)
sock.settimeout(2)

timer = time.time()
fps = 0

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
                data = client_sock.recv(99532800)
                if not data:
                    print('Client disconnected')
                    break
                display.display2(data)
                fps += 1
            except socket.timeout:
                display.close()
                pass
    except socket.error as e:
        display.close()
        print('Error occurred:', e)