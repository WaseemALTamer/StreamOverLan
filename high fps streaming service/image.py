from PIL import Image
import numpy as np
import dxcam
import mss
import cv2
import time
import io



video_runing = False



def run():
    global cap
    cap = cv2.VideoCapture(0)
    time.sleep(2)

def get():
    global image
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




def screenshot1(prefomence_mode):
    global camera,video_runing
    if video_runing == False:
        camera = dxcam.create(device_idx=0, output_idx=0)
        camera.start(target_fps=120, video_mode=True)
        video_runing = True
    img = camera.get_latest_frame()
    return convert(img)



def screenshot(prefomence_mode):
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        img= cv2.resize(img, (1280, 720))
        return convert(img)

