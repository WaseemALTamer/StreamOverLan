import socket
import image
import sys
import time
import pygame

server_address = ('192.168.1.173', 1234)

fps = 0
timer = time.time() + 1

#image.run()

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        print('Connected to the server')
        while True:
            if time.time() > timer:
                print(fps)
                fps = 0
                timer = time.time() + 1
            try:
                message = image.screenshot1(True)
                #message = image.convert(image.get()[0])
                sock.sendall(message)
                fps += 1
                #pygame.time.wait(5)
            except OSError as e:
                print(f'An error occurred: {e}')
                break
            except KeyboardInterrupt:
                break
            except:
                print('Unexpected error:', sys.exc_info()[0])
                break

    except ConnectionRefusedError:
        print('Connection refused. Retrying in 2 seconds...')
        time.sleep(2)
        continue

    except Exception as e:
        print(f'An error occurred: {e}')
        break