import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet7")




df["date2"] = ["2020-03",
"2020-04",
"2020-05",
"2020-06",
"2020-07",
"2020-08",
"2020-09",
"2020-10",
"2020-11",
"2020-12",
"2021-01",
"2021-02",
"2021-03"]

del df["date"]



df.set_index("date2")

df = df.rename(columns={"date2": "date", "return": "return"})









x = df["date"]
y1 = df["return"]


width = 1.0











x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y1)
plt.xticks(x_pos, x)



plt.xlabel("date",fontsize=20)
plt.ylabel("percentage", fontsize=20)




plt.legend(loc="best", prop={"size":15})





plt.xlabel("Date", fontsize=16)
plt.ylabel("Rendement (%)", fontsize=18)
plt.title("Rendement mensuel du Portefeuille depuis 1 an", fontsize=23)
plt.show()

plt.rcParams["figure.figsize"] = [16,9]
