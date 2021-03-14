import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet2")


df["Date"] = pd.to_datetime(df["Date"], format = "%d/%m/%Y")




df.set_index("Date")

df = df.rename(columns={"draw port": "Maximum drawdown Portefeuille", "draw SP500": "Max drawdown S&P500"})


x = df["Date"]
y1 = df["Maximum drawdown Portefeuille"]
y2 = df["Max drawdown S&P500"]



plt.plot(x, y1, label = "Portefeuille", linewidth = 2)
plt.plot(x, y2, label = "S&P500", linewidth = 2)

plt.xlabel("Date",fontsize=20)
plt.ylabel("Drawdown (%)", fontsize=20)

plt.rcParams["axes.xmargin"] = 0
plt.rcParams["axes.ymargin"] = 0


plt.legend(loc="best", prop={"size":15})


plt.title(label="Maximum drawdown", fontsize=25)


plt.show()

plt.rcParams["figure.figsize"] = [16,9]


