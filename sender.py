import socket
import image
import time
ip = "192.168.1.171"
port = 5005
buffer = 921600

uav = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cap = image.convert(image.screenshot())
    image.save("photo.jpg")
    n = len(cap)
    segment_length = n // 4
    segments = [cap[i:i+segment_length] for i in range(0, n, segment_length)]
    print([len(s) for s in segments])
    for i in range (0, len(segments)):
        time.sleep(1/144)
        uav.sendto(segments[i], (ip, port))
    uav.sendto("frame".encode(), (ip, port))
    print("frame")
