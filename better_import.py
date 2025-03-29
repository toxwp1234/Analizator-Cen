import yfinance as yf
import pandas as pd

###Nazwa pliku

file_name : str = "data.txt"


open(file_name, 'w').close()

##od którego roku?
start_year = 2020
## do którgo roku
end_year = 2024


#statystyki
iterval = "1D"
period = None
symbol = rf"%5ENDX"

# 5EGSPC - US500

# %5ENDX - US100




months= {"01":"31",
         "02":"28",
         "03":"31",
         "04":"30",
         "05":"31",
         "06":"30",
         "07":"31",
         "08":"31",
         "09":"30",
         "10":"31",
         "11":"30",
         "12":"31"
}

#"2024-11-14"

#program leci przez wszytkie daty dzienne 
#od podanej daty


file = open(file_name,"a")
for year in range(start_year,end_year+1):
    for curr_month in months:
       
        get_id_start = str(year)+"-"+curr_month+"-"+"01"
        get_id_end = str(year)+"-"+curr_month+"-"+months[curr_month]


        #tworze ticket
        Ticket = yf.Ticker(symbol)
        ticket_info = Ticket.history(period=period,start=get_id_start,end=get_id_end,interval=iterval)
        
        open_close = ticket_info[["Open","Close",]]
        #print(open_close)
        num_of_rows = len(open_close)
        ### dostałem info o miesiącu dziennie - teraz przelatuje każdy dzień i dodaje go do pliku
        for r in range(num_of_rows):
            P_open = round(open_close["Open"][r],4)
            P_close = round(open_close["Close"][r],4)
            file.write(f"{P_open};{P_close}\n")
    print(f"{year} {curr_month}")

            


file.close()
print("SUCCES")

        






        