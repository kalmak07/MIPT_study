import RPi.GPIO as GPIO
import time

LED = 26
FREQ = 200
STEP = 1.0
DELAY = 0.05

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, FREQ)
duty = 0.0
pwm.start(duty)

try:
    while True:
        pwm.ChangeDutyCycle(duty)
        time.sleep(DELAY)
        duty += STEP
        if duty > 100.0:
            duty = 0.0
finally:
    pwm.stop()
    GPIO.cleanup()