import mcp4725_driver as mcp
import time

# Параметры сигнала
amplitude = 4.8        # Амплитуда (0–5 В)
frequency = 10         # Частота в Гц
sample_rate = 1000     # Частота дискретизации

# Расчёт шага
period = 1.0 / frequency
samples = int(period * sample_rate)
step = 2 * amplitude / samples

try:
    # Инициализация ЦАП
    dac = mcp.MCP4725(5.0, verbose=False)
    
    value = 0
    direction = 1
    
    while True:
        # Установка напряжения
        dac.set_voltage(value)
        
        # Изменение значения
        value += direction * step
        if value >= amplitude:
            value = amplitude
            direction = -1
        elif value <= 0:
            value = 0
            direction = 1
        
        # Пауза
        time.sleep(1.0 / sample_rate)
        
except KeyboardInterrupt:
    print("\nОстановлено")
finally:
    dac.deinit()