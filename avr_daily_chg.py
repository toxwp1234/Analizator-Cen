import copy



file = open("dzienne_custom_year","r")

t=0

##tworze listy cen otwarcia i zamknięcia

open_prices=[]
close_prices=[]
#lece przez kazdą linijke pliku z cenami pobieram dane linia po lini i splituje
for line in file:
    prices=line
    ceny=prices.split("\n")[0]
    open_prices.append(ceny.split(";")[0])
    close_prices.append(ceny.split(";")[1])
    #print(ceny.split(";"))



#tworze petle i liste zmiany --- bede tu liczył każdą zależność --
## licze zmiane zależną od podanej podziałce danych (srd zmiana dzienna dla dziennych info)
## dla weekly danych bedzie pokazana srednia zmiana tygodniowa itd


change = []
for i in range (len(open_prices)):
    zmiana = float(close_prices[i]) - float(open_prices[i])
    start_price = float(open_prices[i])
    change_pp : float = round(zmiana*100/start_price,3)
    change.append(change_pp)


change.sort()
print(f"ile wejsc : {len(change)}\n\n")
negative_count: int =0
negative_wholePP: float = 0

postive_count: int = 0
positive_wholePP: float = 0


wzrosty = []
spadki = []

print()
#petla liczaca spadki i wzorsy|| dodaje i towrzy nowe listy na spadki i wzrosty
for cena in change:
    if(cena<0):
        negative_count+=1
        negative_wholePP+=cena
        spadki.append(cena)
    else:
        postive_count+=1
        positive_wholePP+=cena
        wzrosty.append(cena)

#srednia zaookraglona do 3
avr_up = round(float(positive_wholePP/postive_count),3)
avr_down = round(float(negative_wholePP/negative_count),3)

print(f"Jest {postive_count} zwyzek o sredniej wartosci {avr_up}")
print(f"Jest {negative_count} spadkow o sredniej wartosci {avr_down}")



##ilosc spadków
rise_num = postive_count
fall_num = negative_count

print()
###Sparawdzam ile % cen było większych niż jeden 1%

#wprowadzam dane dla którcyh ceny chce wiedzieć
basis = [0.3,0.5,1,2,3]#... # może byc dowolna liczba 
basis.sort()

def get_procent(start_num,end_num):


    ### get_procent(10,3) --> 3/10 = 30.0000



    return(round(float(end_num*100/start_num),4))


#petla główna - liczy ile bylo wzrostów większych od X || nasteonie ti sano dla spadków
for proc in basis:

    liczba_wzr : int = 0
    wartosc_wzr : float = 0 
    for cena in wzrosty:
        if(cena>=proc):
            liczba_wzr+=1
            wartosc_wzr+=cena
    
    
    print(f"{get_procent(postive_count,liczba_wzr)} % wzrostow bylo wiekszych od {proc}% --- tylko {liczba_wzr}")
print()
for proc in basis:

    liczba_spad : int = 0
    wartosc_spad : float = 0 
    for cena in spadki:
        if(cena<=-proc):
            liczba_spad+=1
            wartosc_spad+=cena
    print(f"{get_procent(negative_count,liczba_spad)} % spadkow bylo wiekszych od {proc}% --- tylko {liczba_spad}")



basis_value =[1,2,3,4]

# # obliczam ile % wzrostów było większych od x
# for val_x in basis_value:
#     ile_wiekszych : int = 0 

#     for watrosc_wzrostu in wzrosty:
#         if(val_x>=watrosc_wzrostu):
#             ile_wiekszych+=1
    
#     print(f"{get_procent(postive_count,ile_wiekszych)}")





































