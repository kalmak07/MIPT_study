import RPi.GPIO as GPIO
import time

LED = 26
BUTTON = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

state = 0
GPIO.output(LED, state)

try:
    while True:
        if GPIO.input(BUTTON):
            state = not state
            GPIO.output(LED, state)
            time.sleep(0.2)
finally:
    GPIO.cleanup()