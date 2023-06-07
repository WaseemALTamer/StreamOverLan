import image
import display
import time

fps = 0
timer = time.time() + 1
x = image.screenshot1(True)


while True:
    if time.time() >= timer:
        print(fps)
        fps = 0
        timer += 1
    fps += 1  
    display.display(x)
