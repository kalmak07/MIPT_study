import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 4.8
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(5.0, verbose=False)
    
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
