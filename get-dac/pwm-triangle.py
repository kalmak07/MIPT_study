import pwm_dac as pwm
import time

amplitude = 3.2
frequency = 10
sample_rate = 1000

period = 1.0 / frequency
samples = int(period * sample_rate)
step = 2 * amplitude / samples

try:
    dac = pwm.PWM_DAC(12, 500, 3.29, verbose=False)
    
    value = 0
    direction = 1
    
    while True:
        dac.set_voltage(value)
        
        value += direction * step
        if value >= amplitude:
            value = amplitude
            direction = -1
        elif value <= 0:
            value = 0
            direction = 1
        
        time.sleep(1.0 / sample_rate)
        
except KeyboardInterrupt:
    pass
finally:
    dac.deinit()