import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.29, verbose=False)
    
    t = 0
    while True:
        norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = norm_amp * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1.0 / sampling_frequency
        
except KeyboardInterrupt:
    pass
finally:
    dac.deinit()