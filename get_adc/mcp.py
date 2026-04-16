import mcp3031_driver
import time
import adc_plot

xs = []
ys = []
totallen = 8
t = time.time()
tc = 0
ts = []

if __name__ == "__main__":
    try:
        adc = mcp3031_driver.MCP3021(5)
        while time.time() - t < totallen:
            try:
                tc = time.time()
                ys.append(adc.get_voltage())
                xs.append(time.time()-t)
                ts.append(time.time()-tc)
            except ValueError:
                print("error")
    finally:
        adc.deinit()

adc_plot.plot(xs,ys)
adc_plot.plot_hist(ts)