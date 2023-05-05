from PIL import Image
import numpy as np
import pyautogui
import cv2
import time
import io

def run():
    global cap
    cap = cv2.VideoCapture(0)
    time.sleep(2)

def get(FPS):
    global image
    time.sleep(1/FPS)
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return image, ret

def show():
    global image
    pillow_image = Image.fromarray(np.uint8(image))
    pillow_image.show()

def save(filename):
    global image
    pillow_image = Image.fromarray(np.uint8(image))
    pillow_image.save(filename)


def end():
    global cap
    cap.release()


def convert(photo):
    pil_image = Image.fromarray(np.uint8(photo))
    with io.BytesIO() as output:
        pil_image.save(output, format="JPEG")
        jpeg_bytes = output.getvalue()
        return jpeg_bytes

def screenshot():
    global image
    image = np.array(pyautogui.screenshot())
    return image