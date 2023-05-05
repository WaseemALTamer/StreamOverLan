import numpy as np
import cv2

def display(photo_data):
    try:
        jpg_data = np.frombuffer(photo_data, dtype=np.uint8)
        img = cv2.imdecode(jpg_data, cv2.IMREAD_COLOR)
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return quit()
    except:
        pass   
