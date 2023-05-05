import socket
import display

receiver_ip = '192.168.1.171'
receiver_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1/10)
sock.bind((receiver_ip, receiver_port))

packs = []
frame_received = False

while True:
    try:
        data, addr = sock.recvfrom(65536)
        if b"frame" in data:
            if not frame_received:
                frame_received = True
            else:
                # Concatenate all the packets received so far
                photo = b''.join(packs)
                try:
                    display.display(photo)
                except OSError as e:
                    print("System Error")
                    sock.close()
                    pass
                except KeyboardInterrupt:
                    print("Keyboard Interrupted")
                    sock.close()
                    pass
                # Clear the list of packets
                packs.clear()
        else:
            packs.append(data)
    except socket.timeout:
        with open("range.jpg", 'rb') as f:
            photo_data = f.read()
        display.display(photo_data)
        pass