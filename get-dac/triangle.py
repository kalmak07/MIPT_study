import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self, vref):
        self.vref = vref
        self.leds = [16, 12, 25, 17, 27, 23, 22, 24]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.leds, GPIO.OUT)
        GPIO.output(self.leds, 0)
    
    def set_value(self, value):
        bits = [int(bit) for bit in bin(value)[2:].zfill(8)]
        GPIO.output(self.leds, bits)
    
    def __del__(self):
        GPIO.output(self.leds, 0)

if __name__ == "__main__":
    try:
        dac = R2R_DAC(3.3)
        
        amplitude = 255
        frequency = 10
        sample_rate = 1000
        
        period = 1.0 / frequency
        samples = int(period * sample_rate)
        step = 2 * amplitude / samples
        
        value = 0
        direction = 1
        
        while True:
            dac.set_value(int(value))
            
            value += direction * step
            if value >= amplitude:
                value = amplitude
                direction = -1
            elif value <= 0:
                value = 0
                direction = 1
            
            time.sleep(1.0 / sample_rate)
            
    finally:
        GPIO.cleanup()
