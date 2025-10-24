import RPi.GPIO as GPIO
import time
from rpi_lcd import LCD
import random
import string

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(16,GPIO.OUT)

screen = LCD()
screen.backlight(True)

def goCrazy():
    i = 0
    while i < 50:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)
        i += 1

def rig(rigged):
    
    if GPIO.input(21) == 0:
        if not rigged:
            GPIO.output(16,GPIO.HIGH)
            rigged = True
        else:
            GPIO.output(16,GPIO.LOW)
            rigged = False
        time.sleep(0.5)
    return rigged



def slot(ri):
    num = random.choice(string.ascii_letters)
    if ri:
        num = "A"
    return num

def wait(r):
    while GPIO.input(19) == 1:
        
        r = rig(r)
        time.sleep(0.1)
    return r


def main():
    jackpot = False
    try:
        
        while True:
            
            jackpot = wait(jackpot)

            s1 = slot(jackpot)
            s2 = slot(jackpot)
            s3 = slot(jackpot)
            s4 = slot(jackpot)

            
            while GPIO.input(19) == 0:
                rolling = ''.join(random.choices(string.ascii_letters, k = 4))
                screen.text(rolling, 1)
                time.sleep(0.1)
            screen.text(s1 + s2 + s3 + s4, 1)
            if s1 == s2 and s1 == s3 and s1 == s4:
                goCrazy()
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        screen.clear()
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
    
main()