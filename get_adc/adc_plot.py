import matplotlib.pyplot as plt

def plot(xs, ys):
    #plt.plot([xs[i],xs[i+1]],[ys[i],ys[i+1]],color="blue")
    plt.plot(xs,ys,color="blue")  

    plt.show()

def plot_hist(ts):
    plt.figure(figsize=(10,6))
    plt.hist(ts)
    plt.show()