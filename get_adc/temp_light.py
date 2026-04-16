import time
import mcp3031_driver as mcp
import math

VREF = 5.0
OFFSET = 0.5
SCALE = 0.01
RFIXED = 10000.0
MINR = 1000.0
MAXR = 1000000.0

def temp(v):
    return (v - OFFSET) / SCALE

def light(v):
    if v <= 0.01:
        return 0.0
    if v >= VREF - 0.01:
        return 100.0
    r = RFIXED * (VREF - v) / v
    if r <= MINR:
        return 100.0
    if r >= MAXR:
        return 0.0
    return 100.0 * (math.log10(MAXR) - math.log10(r)) / (math.log10(MAXR) - math.log10(MINR))

if __name__ == "__main__":
    adc = mcp.MCP3021(VREF)
    try:
        while True:
            v = adc.get_voltage()
            print("Temp: {:.2f} C  Light: {:.1f} %".format(temp(v), light(v)))
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        adc.deinit()