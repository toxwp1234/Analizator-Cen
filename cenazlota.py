import yfinance as yf
import pandas as pd

pd.options.mode.copy_on_write = True


AU = "GC=F"
interval = '1d'
start_date = "2024-01-01"
end_date = "2024-11-14"
period = None

zloto = yf.Ticker(AU)




zloto_hour = open("zloto_1h.txt",'w')
zloto_hour.write("\n")
zloto_hour.close()
zloto_hour = open("zloto_1h.txt",'a')

# otweram plik





zloto_info = zloto.history(period=period,start=start_date,end=end_date,interval="1h")
#print(zloto_info)
number_in_list=len(zloto_info) # liczba wejśc



OC_zloto=zloto_info[["Open","Close"]] # definicja bazy panda tylko z kolumnami otwracia i zamknięcia




OC_zloto["Change"]=round((OC_zloto["Close"]-OC_zloto["Open"])/OC_zloto["Open"] *100,2)




ceny_O_C_P =[] #Tworze liste która trzyma C_otwarcia,C_zamknięcia,%zmiany w takiej kolejności
loop = 0    # Tworze zmianną która bedzie mi pomagała w printowaniu co 3 zmiennej




# pętla gdzie wydobywam cene otwarcia zamkniecia i zmiant% dodając je do listy



for r in range(number_in_list):

    open_price = OC_zloto["Open"][r]
    close_price = OC_zloto["Close"][r]
    change_proc = OC_zloto["Change"][r]

#     #historia
#     # ceny_O_C_P.append(round(open_price,4))
#     # ceny_O_C_P.append(round(close_price,4))
#     # ceny_O_C_P.append(round(change_proc,2))
#     #zmiana planów - zamiast wykorzystać listę dodam do pliku odpowiednie liczby w kolejności
   
    sender = f"{round(open_price,4)}:{round(close_price,4)}:{round(change_proc,2)};"
    print(sender)
    zloto_hour.write(sender)
    zloto_hour.write("\n")

else:
    print("Success")

zloto_hour.write(str(number_in_list))
zloto_hour.close()


#     print()
# zloto_hour.close()
#     #loop+=3





























#print(OC_zloto.to_string())

#print(float(OC_zloto["Open"][1]))






   # OC_zloto["Change%"] = 1 #delta/OC_zloto["Open"][x]*100
    

# print(OC_zloto["Open"])
# print(OC_zloto["Open"][0])







# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data)

# print(df)

# print(df['calories'].to_string(index=False))





