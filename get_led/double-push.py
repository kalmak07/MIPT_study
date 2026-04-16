import RPi.GPIO as GPIO
import time

LEDS = [16, 12, 25, 17, 27, 23, 22, 24]
UP_PIN = 5
DOWN_PIN = 19
SLEEP_TIME = 0.2

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(UP_PIN, GPIO.IN)
GPIO.setup(DOWN_PIN, GPIO.IN)

num = 0
GPIO.output(LEDS, dec2bin(num))

try:
    while True:
        up = GPIO.input(UP_PIN)
        down = GPIO.input(DOWN_PIN)
        if up and down:
            num = 255
            print(num, dec2bin(num))
            GPIO.output(LEDS, dec2bin(num))
            time.sleep(SLEEP_TIME)
        elif up:
            num = num + 1 if num < 255 else 0
            print(num, dec2bin(num))
            GPIO.output(LEDS, dec2bin(num))
            time.sleep(SLEEP_TIME)
        elif down:
            num = num - 1 if num > 0 else 255
            print(num, dec2bin(num))
            GPIO.output(LEDS, dec2bin(num))
            time.sleep(SLEEP_TIME)
finally:
    GPIO.cleanup()