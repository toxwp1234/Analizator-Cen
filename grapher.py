import matplotlib.pyplot as plt
import numpy as np



#download_data

##nazwy pliów otwieranych mogą być zmienine
file_day = open("data.txt","r")
file_trend = open("trends_data.txt","r")


# OP - open price 
# CP - close price 
# OP_day - realny graf
# OP_trend - ruchy main graf



#pobieram dane dzienne
OP_day : list = []
CP_day : list = []
for line in file_day:
    line = line.split()[0].split(";")
    OP_day.append(float(line[0]))
    CP_day.append(float(line[1]))

# print(dict(enumerate(CP_day)))


ruchy :list = []

#pobieram dane z duzych ruchów


for line in file_trend:
    prices=line
    ceny=prices.split("\n")[0]
    cena_open : float= ceny.split()[0]
    cena_close : float = ceny.split()[1]
    start_day :int = ceny.split()[4]
    end_day :int = ceny.split()[5]
    up_trend :bool = ceny.split()[3]

    adder = [cena_open,cena_close,start_day,end_day,up_trend]
    ruchy.append(adder)
    


# print(ruchy[1])


#rozdzielam dane na dni i ich ceny zamknięcia

x_trend : list =[]
y_trend : list = []
test : dict= {}


for element in ruchy:
    
    x_trend.append(float(element[2]))
    y_trend.append(float(element[0]))
    test[element[2]] = element[0]

print(len(x_trend))
print(len(y_trend))


# print(test)

x_val : list = list(i for i in range(len(CP_day)))



plt.plot(x_val, CP_day,color="dodgerblue")
plt.plot(x_trend, y_trend,color="red") 


  # Plot some data on the Axes.
plt.show()                           # Show the figure.

    
