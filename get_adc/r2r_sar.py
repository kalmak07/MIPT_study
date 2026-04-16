import r2r_adc
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
        adc = r2r_adc.R2R_ADC(3.3, 0.01)
        while time.time() - t < totallen:
            try:
                tc = time.time()
                ys.append(adc.sar_approx_vlt())
                xs.append(time.time()-t)
                ts.append(time.time()-tc)
            except ValueError:
                print("error")
    finally:
        adc.deinit()

adc_plot.plot(xs,ys)
adc_plot.plot_hist(ts)