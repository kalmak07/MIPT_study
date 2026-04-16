import RPi.GPIO as GPIO
import time

LEDS = [24, 22, 23, 27, 17, 25, 12, 16]
LIGHT_TIME = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS, GPIO.OUT)
GPIO.output(LEDS, 0)

try:
    while True:
        for led in LEDS:
            GPIO.output(led, 1)
            time.sleep(LIGHT_TIME)
            GPIO.output(led, 0)
        for led in reversed(LEDS):
            GPIO.output(led, 1)
            time.sleep(LIGHT_TIME)
            GPIO.output(led, 0)
finally:
    GPIO.cleanup()