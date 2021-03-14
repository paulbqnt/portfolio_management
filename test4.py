import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("data.xlsx", sheet_name="Sheet3")

df["date"] = pd.to_datetime(df["date"], format = "%m/%d/%Y")

df.set_index("date")


df = df.rename(columns={
"ishares us financials": "US financials",
"ishares us telecommunications": "US telecommunications",
"ishares us industrials": "US industrials",
"ishares us consumer services": "US consummer services",
"ishares us consumer goods": "US consumer goods",
"ishares us utilities": "US utilities",
"ishares us basic materials": "US basic materials",
"ishares us energy": "US energy",
"ishares russell 2000": "Russel 2000",
"spdr sp 500": "S&P 500",
"ishares sp 500 growth": "S&P 500 growth",
"ishares sp 500 value": "S&P 500 value",
"Apple": "Apple",
"Johnson & Johnson": "Johnson & Johnson",
"Berkshire Hathaway inc A": "Berkshire Hathaway",
"Cash": "Cash"})



labels = [
"12/31/2010",
"12/31/2011",
"12/31/2012",
"12/31/2013",
"12/31/2014",
"12/31/2015",
"12/31/2016",
"12/31/2017",
"12/31/2018",
"12/31/2019",
"12/31/2020",
"3/9/2021"]

    
    


width = 0.35

fig, ax = plt.subplots()

ax.bar(labels, df["US financials"], width, label = "US financials")
ax.bar(labels, df["US telecommunications"], width, label = "US telecommunications")
ax.bar(labels, df["US industrials"], width, label = "US industrials")
ax.bar(labels, df["US consummer services"], width, label = "US consummer services")
ax.bar(labels, df["US consumer goods"], width, label = "US consumer goods")
ax.bar(labels, df["US utilities"], width, label = "US utilities")
ax.bar(labels, df["US basic materials"], width, label = "US energy")
ax.bar(labels, df["Russel 2000"], width, label = "Russel 2000")
ax.bar(labels, df["S&P 500"], width, label = "S&P 500")
ax.bar(labels, df["S&P 500 growth"], width, label = "S&P 500 growth")
ax.bar(labels, df["Apple"], width, label = "Apple")
ax.bar(labels, df["Johnson & Johnson"], width, label = "Johnson & Johnson")
ax.bar(labels, df["Berkshire Hathaway"], width, label = "Berkshire Hathaway", color = "coral")
ax.bar(labels, df["Cash"], width, label = "Cash")

plt.legend(loc="best")


plt.title(label = "Historical sector weighting of Portfolio")



plt.rcParams["figure.figsize"] = (20,10)

ax.set_ylabel("Percentage", fontsize = 15)
ax.set_xlabel("Date", fontsize = 15)
ax.set_title("Historical sector weighting of Portfolio", fontsize=20)
ax.legend()
plt.show()





    
"""
x = df["date"]


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
"""
