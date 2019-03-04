from PIL import ImageGrab
import time
import socket

QUALITY = 500
## Socket setup
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


def inf_loop():
    screen = ImageGrab.grab()
    pix = screen.load()
    w, h = screen.size

    i = 0
    j = 0
    avg = (0,0,0)


    avg = pix[0,0]

    while i < (w-1):
        i = i + QUALITY
        j = 0
        while j < (h-1) and i < (w-1):
            avg = ((avg[0]+pix[i,j][0])/2,(avg[1]+pix[i,j][1])/2,(avg[2]+pix[i,j][2])/2)
            j = j + QUALITY

    print avg
    return avg

def send(message):
    

while True:
    send(inf_loop())
    time.sleep(1)
