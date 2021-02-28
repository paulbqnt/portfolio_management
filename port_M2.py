import pandas as pd
import investpy

# utilisation d’un tuple par sécurité (tuple = liste figée non modifiable)
liste_etf = ("iShares us Financials", "iShares us Telecommunications", "iShares US Industrials",
             "iShares US Consumer Services",
             "iShares US Consumer Goods", "iShares US Utilities", "iShares US Basic Materials", "iShares US Energy")

liste_stock = ("TSLA", "AAPL", "JNJ")

# Python n’acceptant pas les espaces, 
new_liste = []
for i in liste_etf:
    new_liste.append(i.lower().replace(" ", "_"))


    
    
    

# Creation des Data Frames
for etf in liste_etf:
    vars()[etf.lower().replace(" ", "_")] = pd.DataFrame(
        investpy.etfs.get_etf_historical_data(etf, "united states", "01/01/2009","01/01/2021", 
                                              stock_exchange=None, 
                                              as_json=False, 
                                              order="ascending",
                                              interval="Daily"))
    
for stock in liste_stock:
    vars()[stock.lower()] = pd.DataFrame(
        investpy.stocks.get_stock_historical_data(stock, "united states", "01/01/2009", "01/01/2021",
                                                  as_json=False,
                                                  order="ascending",
                                                  interval="Daily"))

new_liste = ['ishares_us_financials', 'ishares_us_telecommunications', 'ishares_us_industrials', 'ishares_us_consumer_services', 'ishares_us_consumer_goods', 'ishares_us_utilities', 'ishares_us_basic_materials', 'ishares_us_energy', "tsla", "aapl", "jnj"]



# Conversion du format date des Data Frames
for item in new_liste:
    exec(f"{item}.index = {item}.index.strftime('%d/%m/%Y')")
    

writer = pd.ExcelWriter("portfolio.xlsx", engine = "xlsxwriter")


# Excel ws name must be <= 31 characters
# itteration dans la liste pour retirer les 11 premiers caracteres
#short_liste = [e[:16] for e in new_liste]




# Creation du fichier excel dans le working directory du fichier port_M2.py
for item in new_liste:
    #for x in short_liste:
    exec(f"{item}.to_excel(writer, sheet_name='{item}')")

writer.save()




