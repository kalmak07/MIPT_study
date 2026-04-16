import RPi.GPIO as GPIO
import time

LED = 26
PERIOD = 1.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

state = 0

try:
    while True:
        GPIO.output(LED, state)
        state = not state
        time.sleep(PERIOD)
finally:
    GPIO.cleanup()