from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import numpy as np
import time

data = ""
timer = time.time() + 1
fps = 0
display_fps = 0


def display(photo_data):
    global timer, fps, data
    if photo_data == b"":
        return None
    try:
        jpg_data = np.frombuffer(photo_data, dtype=np.uint8)
        img = cv2.imdecode(jpg_data, cv2.IMREAD_COLOR)
        cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
        cv2.imshow('Window', img)
        cv2.waitKey(1)
        if timer < time.time():
            fps = 0
            timer = time.time() + 1
        fps += 1
    except:
        pass
    
def close():
    cv2.destroyAllWindows()
