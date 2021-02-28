import pandas as pd
import investpy

# utilisation d’un tuple par sécurité (tuple = liste figée non modifiable)
liste_etf = ("iShares us Financials", "iShares us Telecommunications", "iShares US Industrials",
             "iShares US Consumer Services",
             "iShares US Consumer Goods", "iShares US Utilities", "iShares US Basic Materials", "iShares US Energy")


# Python n’acceptant pas les espaces, 
new_liste = []
for i in liste_etf:
    new_liste.append(i.lower().replace(" ", "_"))

# Creation des Data Frames
for etf in liste_etf:
    vars()[etf.lower().replace(" ", "_")] = pd.DataFrame(
        investpy.etfs.get_etf_historical_data(etf, "united states", "01/01/2010","01/01/2021", 
                                              stock_exchange=None, 
                                              as_json=False, 
                                              order="ascending",
                                              interval="Daily"))


# Conversion du format date des Data Frames
for item in new_liste:
    exec(f"{item}.index = {item}.index.strftime('%d/%m/%Y')")
    

writer = pd.ExcelWriter("pandas_multiple.xlsx", engine = "xlsxwriter")


# Excel ws name must be <= 31 characters
# itteration dans la liste pour retirer les 11 premiers caracteres
short_liste = [e[11:] for e in new_liste]

# Creation du fichier excel dans le working directory du fichier port_M2.py
for item in new_liste:
    for x in short_liste:
        exec(f"{item}.to_excel(writer, sheet_name='{x}.excel')")

writer.save()




