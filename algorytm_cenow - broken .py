###
### Celem tego algortmu jest znalezienie punktów najwyższych i najniższych z odpowiednim
### parametrem zawierającym długość trendu
### ZAKŁOZENIE ::: musi być więcej danych niż 2


### Najpier pobieram dane -- cena otwarcia i cena zamknięcia

file = open("dzienne_custom_year","r")

#listy otwarcia i zamknięcia
open_price = []
close_price = []

for line in file:
    line = line.split()[0].split(";")
    open_price.append(line[0])
    close_price.append(line[1])



## skrypt


lowest : float = close_price[0]
highest : float= close_price[0]

highest_ID = 0
lowest_ID = 0

latest_ID : int = 0

starting_ID : int = 0 # potrzebna jest ta funkcja do sprawdzania globalnej zmiany od poprzedniego szczytu


temp_High: float = close_price[0]
temp_Low: float = close_price[0]

 
### zdefinuje parę funkcji które pomogą mi czytalniej napisać kod



high_list_ID = []
low_list_ID = []


timer_limit : int = 4 ### zasięg bez zmiany cen 

timer = 0

flaga=True

i : int = 0


been = set()



while flaga == True and i<=10000:
    #print(i)
    now : float = close_price[i]
    ### i to indeks na której cenie jestem

    
    if(i>=len(close_price)-1):

        # q_dic = {starting_ID:close_price[starting_ID], latest_ID:close_price[latest_ID]}

        # high_list_ID.append(max({))
        #pierdole tą dokładnośc od startowego id fo teraz
        if(close_price[starting_ID]>close_price[i]):
            high_list_ID.append(starting_ID)
            low_list_ID.append(i)
        else:
            high_list_ID.append(i)
            low_list_ID.append(starting_ID)
             


        flaga=False

    #jak osiągam nowy szczyt
    if(now > highest):
        highest = now
        highest_ID = i
        #zapisuje najaktualniejsze id
        latest_ID = i
        timer = 0


    elif(now <= lowest):

        lowest=now
        lowest_ID=i
        #zapisuje najaktualniejsze id
        latest_ID = i
        timer = 0
    

    #jeżeli jestem nad minimum i pod maksimum i w limicie => dodaje jeden do timera 
    elif(now <= highest and now > lowest and timer<=timer_limit):
        timer+=1
    

    #jeżeli wyjde za czas --- zapisuje ostatnie minimum i ostatnie maksimum i cofam sie do ostatniego id maksimum
    elif(timer > timer_limit):
        


        if((close_price[highest_ID] == close_price[starting_ID]) or (close_price[lowest_ID] == close_price[starting_ID])):

                #Zapisuje indeksy cen najwyższych i najnizszych
            #Po czym przesuwam moją pozycje do ostatnio zapisanego indeksu

            high_list_ID.append(highest_ID)
            low_list_ID.append(lowest_ID)

            i = latest_ID - 1 # uwzgledniam dodanie jedynki pod koniec pętli

            #ustawiam pozycje startową nową
            starting_ID = i
            highest=close_price[i]
            lowest=close_price[i]
        
        else : #jeżeli cena startowa to nie maksimum i nie minimum 
                #sprawdzam co jest highem i lowem względem start_id i latest_id

            if(close_price[starting_ID]>close_price[latest_ID]):

                #higest to star a low to latest

                high_list_ID.append(starting_ID)
                low_list_ID.append(latest_ID)

                i = latest_ID - 1 # uwzgledniam dodanie jedynki pod koniec pętli

                #ustawiam pozycje startową nową
                starting_ID = i+1
                highest=close_price[i+1]
                lowest=close_price[i+1]

            else:

                # high_list_ID.append(close_price[latest_ID])
                # low_list_ID.append(close_price[starting_ID])

                high_list_ID.append(latest_ID)
                low_list_ID.append(starting_ID)
                
                i = latest_ID - 1 # uwzgledniam dodanie jedynki pod koniec pętli

                #ustawiam pozycje startową nową
                starting_ID = i+1
                highest=close_price[i+1]
                lowest=close_price[i+1]







        


    ### dodaje +1 do pozycji ceny
    print(i)
    i=i+1

### tworze liste z cenami zamiast indeksów
ceny_low=[]
ceny_high=[]
#otrzymuje wartośc z id do low i high
for ID in low_list_ID:
    ceny_low.append(close_price[ID])

for ID in high_list_ID:
    ceny_high.append(close_price[ID])


LowHigh = []

for i in range(len(high_list_ID)):
    
    LowHigh.append([ceny_low[i],ceny_high[i]])




    
print(LowHigh)



    














# for i in range(close_price):
#     priceNow = close_price[i]
    
#     if(priceNow<lowest and m<Param): #sprawdzam czy cena jest moim nowym najnizszym i czy minął czas parametru
#         lowest=priceNow
#         iL = i #zapisuje indeks najmniejszego
#         m=0
#     elif(priceNow>highest and m<Param): # sprawdzam czy cena jest moją najwyższa
#         highest=priceNow
#         iH = i # zapisuje indeks najwyzszego
#         m=0
    #dodaje do zminnej czasu
    #t+=1
    





#print(len(open_price),len(close_price))