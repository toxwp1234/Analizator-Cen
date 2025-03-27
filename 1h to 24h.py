import yfinance as yf


cena_1h = open("zloto_1h.txt",'r')

ceny=cena_1h.read().split(";")

number_of_elements = int(ceny[-1])

### cena=[i]  [0,1,2]

#            0 - open
#            1 - close
#            2 - change

print(ceny[0],ceny[-1])


reps = number_of_elements//24
X=0

conversion = open("cena_zlota.txt","w")
conversion.write("\n")
conversion.close()
conversion=open("cena_zlota.txt","a")


for _ in range(reps):

    open = float((ceny[X].split(":")[0]))
    close = float(ceny[X+23].split(":")[1])
    change = round((close-open)/open * 100,4)

    adder = f"{open}:{close}:{change};"
    conversion.write(adder)
    conversion.write("\n")
    X+=24


    print(open,close,change)

conversion.close()


