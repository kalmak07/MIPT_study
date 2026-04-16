import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D


    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        low = data >> 8
        high = data & 0xFF
        number = (high << 6) | (low >> 2)
        return number
    
    def get_voltage(self):
        return self.get_number()*self.dynamic_range/1023.0;


if __name__ == "__main__":
    try:
        adc = MCP3021(5)
        while True:
            try:
                print(adc.get_voltage())
                time.sleep(0.5)
            except ValueError:
                print("error")
    finally:
        adc.deinit()