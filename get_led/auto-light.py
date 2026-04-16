import RPi.GPIO as GPIO

LED = 26
PHOTO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PHOTO, GPIO.IN)

try:
    while True:
        GPIO.output(LED, not GPIO.input(PHOTO))
finally:
    GPIO.cleanup()