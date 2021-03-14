import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet1")


df["Date"] = pd.to_datetime(df["Date"], format = "%d/%m/%Y")




df.set_index("Date")

df = df.rename(columns={"port": "Portefeuille", "sp_500": "S&P500"})


x = df["Date"]
y1 = df["Portefeuille"]
y2 = df["S&P500"]



plt.plot(x, y1, label = "Portefeuille")
plt.plot(x, y2, label = "S&P500")

plt.xlabel("Date",fontsize=20)
plt.ylabel("Return", fontsize=20)

plt.rcParams["axes.xmargin"] = 0
plt.rcParams["axes.ymargin"] = 0


plt.legend(loc="upper left", prop={"size":15})


plt.title(label="Return du Portefeuille", fontsize=20)


plt.show()

plt.rcParams["figure.figsize"] = [16,9]




