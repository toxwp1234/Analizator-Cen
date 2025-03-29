

### nazwa data.txt  --- jeżeli zmienimy nazwe pliku w better_import tutaj też należy zmienić
file = open("data.txt","r")



#listy otwarcia i zamknięcia
open_price = []
close_price = []

for line in file:
    line = line.split()[0].split(";")
    open_price.append(line[0])
    close_price.append(line[1])

file.close()

Flaga = True

id_up =[]
id_down = []

id = 0

#############################################



#definuje słownik z wszyskimi ruchami
ruchy = [] #[ [cena_start , cena ostatniego , ilośc dni trendu, is_wzrostowy? ,start_id , temp_id] ]

def results_get(starting_id : int,temporary_id : int):

    global close_price ##uzywam id z cenami zamknięcia 
    global ruchy 

    adder=[]
    cena_start : float = close_price[starting_id]  ### cena startowa
    cena_ostania : float = close_price[temporary_id]  ### ostatnie ekstremum
    ilos_dni_trendu :int = -starting_id + temporary_id ## licze ile wektorów wzrostowych jest n1 - n2 
   
    if (float(cena_ostania) > float(cena_start)): #jezeli cena osatniego eks. jest większa od statowej
        
        adder = [cena_start,cena_ostania,ilos_dni_trendu,True,starting_id,temporary_id]
        ruchy.append(adder)
        
        return None
    else:
        
        adder = [cena_start,cena_ostania,ilos_dni_trendu,False,starting_id,temporary_id]
        ruchy.append(adder)

        return None   





##########################################

id_been = set()
id_repeat = set()

move_limit = 30 ## kalibracja czułości zbicia ruchu trendu - wygaszanie



Minimum_days: int  = 14 # trend ma trwać conajmniej n dni albo jest usunięty


#dobrze pokazuje move_limit = 2, min_days = 3

i : int = 0 


#id najwyzsza najnizsza startowa i tymczasowa to id z której zaczynam

start_id = i
temp_id = start_id
highest_id : int = start_id
lowest_id : int  = start_id


ids= set()

m = 0
k=0
hard_cap = 15_100
sequence : list = []

while Flaga == True:


    if(i>=len(close_price)-1):


        results_get(start_id,i)

        Flaga = False
    
    if(k >=hard_cap):
        print("Hardcap reached")
        Flaga=False

    now = close_price[i]
    highest = close_price[highest_id]
    lowest = close_price[lowest_id]


    if(now < lowest):
        #jezeli cena teraz jest mniejsza od minimum 
        #print(f"{i} nowy low")
        lowest_id = i
        temp_id = i
        m = 0 #kasuje licznik

    
    elif(now > highest):
        #print(f"{i} nowy high")
        #jak teraz cena jest wieksza od min to ustawiam jako max
        highest_id = i
        temp_id = i
        m = 0 #kasuje licznik

    elif((now <= highest and now >= lowest) and m < move_limit):
        #jezeli ceny są normalne i w limicie ruchów dodaj 1 do ruchu
        #print(f"{i} ide dalej {m+1}/{move_limit}")
        m+=1

    else:
        #gdy sie skonczy czas

        # print(f"{i} - koniec czasu")


        results_get(start_id,temp_id)

        start_id =temp_id
        highest_id = temp_id
        lowest_id = temp_id
        i = temp_id
        m=0

    
    ids.add(i)
    k+=1
    i+=1






### Przed mergowanierm moge oczyszczyć wykres z małych ruchów cen

#niech usune wszyskie ruchy które trwają mniej niż ILEDNI dni




print(len(ruchy))

for line in ruchy:
    if (line[2]<Minimum_days):
        ruchy.remove(line)


print(len(ruchy))








### 
### Do tego momentu pozysukuje dane o trendach n-dniowych
###
### Niestety pojawia się problem gdy wykrywam kilka jednokierunkowych pod rząd
### powinneinem je zmerować tak więc 

# ['31637.7793', '35867.7773', 4, True, 2390, 2394]
# ['35867.7773', '52633.5352', 66, True, 2394, 2460]
# ['52633.5352', '65992.8359', 43, True, 2460, 2503]

# powinnien wyglądać tak -->


# ['31637.7793','65992.8359', 113, True, 2390, 2503]



# for i in range(len(ruchy)):
#     print(f"{i}.) {ruchy[i]}",end="\n")


### Merging



       

 
# print(len(ruchy))

def merge(array:list):

    k : int = 1_0_0_0_0 #hardcap#
    counter : int = 0

    global close_price

    i :int = 0 #indeks obecnego elementu
    merged_arr : list = []
    Flaga = True
    size = len(ruchy)


    while Flaga == True: ##pętla która leci przez każdy ruch z listy
        

        
        if(i>=size):
            return merged_arr


        kierunek_i = array[i][3] ###kierunek początkowego ruchu
        Flaga_min = True ##aktywuje pętle dla nowego elementu
        #False dół, True góra
        n=i+1
        while Flaga_min == True: ## sprawdzam czy kolejne elementy są w tym samym kierunku
            #print(f"Element {i} sprawdzam oraz {n+1}")

            #print(f"Sprawdzam id {n} dla startu {i}")

            if(n>=size): #jeżeli mój wskaźnik jest poza listą to ustawiam go na jego "-1"
                n=n-1 
                dni:int = array[n][5] - array[i][4]
                merged_arr.append([array[i][0],array[n][1],dni,kierunek_i,array[i][4],array[n][5]])    
                Flaga = False
                Flaga_min = False


            kierunek_next = array[n][3]


            #print(f" {i} - {kierunek_i}, {n} - {kierunek_next}")
            if(kierunek_i != kierunek_next):
            
                # jezeli kierunek następnego elementu jest inny od sprawdzanego
                # to ruszam mój wskaźnik na następny element głównej pętli na n+1
                # *(n+1) ponieważ n był w tym samym ruchu wiec merge bedzie od i do n
        

                #print(f"skracam od {i} do {n-1}")

                dni:int = array[n-1][5] - array[i][4]    
                merged_arr.append([array[i][0],array[n-1][1],dni,kierunek_i,array[i][4],array[n-1][5]])

        
                i = n
                Flaga_min = False

        
            
            n+=1
        counter+=1



        if(counter>k):
            return "HardCap reached"
    
    return merged_arr

test = merge(ruchy)


####zapisuje trendy na pliku
open("trends_data.txt","w").close()
file = open("trends_data.txt","a")



for i in test:
    for ele in i:
        file.write(f"{ele} ")
    file.write("\n")
    




print(len(test))



# for i in range(len(test)):
#     print(f"{i}.) {test[i]}",end="\n")
