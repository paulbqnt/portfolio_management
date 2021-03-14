import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet7")


df["date"] = pd.to_datetime(df["date"], format = "%m/%Y")




df.set_index("date")

df = df.rename(columns={"date": "date", "return": "return"})

datetime_series = pd.Series(
    pd.date_range("2020-03-01", periods=13, freq="m"))



df["date"] = datetime_series.dt.month






"""



x = df["date"]
y1 = df["return"]





width = 1.0











x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y1)
plt.xticks(x_pos, x)



plt.xlabel("date",fontsize=20)
plt.ylabel("percentage", fontsize=20)




plt.legend(loc="best", prop={"size":15})





plt.xlabel("Date", fontsize=18)
plt.ylabel("Rendement (%)", fontsize=18)
plt.title("Rendement annuel du Portefeuille", fontsize=23)
plt.show()

plt.rcParams["figure.figsize"] = [16,9]

"""
