import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet5")


df["date"] = pd.to_datetime(df["date"], format = "%d/%m/%Y")




df.set_index("date")

df = df.rename(columns={"date": "date", "return": "return"})

plt.hist(df["return"])
plt.show()

std = np.std(df["return"], ddof=1)
mean = np.mean(df["return"])

domain = np.linspace(np.min(df["return"]), np.max(df["return"]))

plt.plot(domain, norm.pdf(domain,mean,std),
         label='$\mathcal{N}$' + f'$( \mu \\approx {round(mean)}, \sigma \\approx {round(std)} )$')
plt.hist(df["return"], edgecolor="black",alpha=.5,density=True)

plt.show()






"""
x = df["date"]
y1 = df["alpha"]




plt.plot(x, y1, label = r'$\alpha$', linewidth = 1)


plt.xlabel("date",fontsize=20)
plt.ylabel("percentage", fontsize=20)

plt.rcParams["axes.xmargin"] = 0
plt.rcParams["axes.ymargin"] = 0


plt.legend(loc="best", prop={"size":15})

plt.title("Excess Return vs Benchmark", fontsize = 25)


plt.show()

plt.rcParams["figure.figsize"] = [16,9]
"""

