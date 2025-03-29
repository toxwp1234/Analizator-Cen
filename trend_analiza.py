
# ///Definicja funkcji do mediany

def mediana(arr: list):
    arr.sort()  # Sortujemy listę
    n = len(arr)
    
    if n % 2 == 1:
        return arr[n // 2]  # Jeśli długość jest nieparzysta, zwracamy środkowy element
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2  # Jeśli parzysta, zwracamy średnią dwóch środkowych

# 
# 
# 
# 
# 
# 
# 
# 
# 

file = open("to_sie_sra","r")



ruchy :list = []



for line in file:
    prices=line
    ceny=prices.split("\n")[0]
    cena_open : float= ceny.split()[0]
    cena_close : float = ceny.split()[1]
    dlugosc_trendu :int = ceny.split()[2]
    up_trend :bool = ceny.split()[3]

    adder = [cena_open,cena_close,dlugosc_trendu,up_trend]
    ruchy.append(adder)

    


##rozdzielenie ruchów

uptrends :list = []
downtrends :list = []

##dodaje filtracje które usunie mi trendy które trwają mniej niż min_ruch dni.




min_ruch : int = 0  #minimum trend n dni




stan_RN = [21,26.66]       #dane które teraz chce znaleść ---> //  [ DNI , %-ZMIANA]





proc_list : list = [5,10,2,.5,.9,.8]


val_list:list=[20,5,10,30]






counter : int = 0

for element in ruchy:
    if(element[-1]=="True" and int(element[-2])>= min_ruch ):
        uptrends.append(element)
    elif(element[-1]=="False" and int(element[-2])>= min_ruch ):
        downtrends.append(element)
    else:
        counter+=1
        # print(element)

print(f"Deleted {counter} moves")

print()
print()
print()
print()


def do_it():
    for k in uptrends:
        print(k, end = "\n" )

    print()
    print()
    print()
    print()

    for k in downtrends:
        print(k,end = "\n")




print()
print()
print() 
print()
print()

#algorytm cenowy - względem wzrostu trendu








###         MOJA  SZUKANA

####      [ile dni, ile %]





lista = [10]


#algorytm długości trendu


val_list.sort()



val_list.append(stan_RN[0])     

for val in val_list:

    ilosc_szukanych:int = 0

    for ruch in uptrends:
        #jezeli cena jest powyzej vartosci to dodaje 
        if(int(ruch[-2])>=val):
            ilosc_szukanych+=1
    proc = round(ilosc_szukanych*100/len(uptrends),2)

    print(f"{proc}% zwyzek trwalo wiecej niz {val} dni  -------- ---- {ilosc_szukanych}/{len(uptrends)}")

print()
print()
print() 
print()

for val in val_list:

    ilosc_szukanych:int = 0

    for ruch in downtrends:
        #jezeli cena jest powyzej vartosci to dodaje 
        if(int(ruch[-2])>=val):
            ilosc_szukanych+=1
    proc = round(ilosc_szukanych*100/len(downtrends),2)

    print(f"{proc}% znizekek trwalo wiecej niz {val} dni   ---- {ilosc_szukanych}/{len(downtrends)}")


print()
print()
print()
print()
print() 
print()


def get_change(element:list):


    start_price : float = element[0]
    end_price : float = element[1]

    delta_C:float = float(end_price)-float(start_price)

    change = round(delta_C*100/float(start_price),5)
    return abs(change)



proc_list.sort()
proc_list.append(stan_RN[1])  
for proc in proc_list:

    couter_change : int = 0

    for element in uptrends:
        
        if(get_change(element)>proc):
            couter_change+=1
    
    proc_ch = round(couter_change*100/len(uptrends),5)

    print(f"{proc_ch}% zwyzek bylo wieksze od {proc}%  ---- {couter_change}/{len(uptrends)}")
        

print()
print()



for proc in proc_list:

    couter_change : int = 0

    for element in downtrends:
        
        if(get_change(element)>proc):
            couter_change+=1
    
    proc_ch = round(couter_change*100/len(downtrends),5)

    print(f"{proc_ch}% znizek bylo wieksze od {proc}%  ---- {couter_change}/{len(downtrends)}")



print()
print()
print() 
print()


print()
print()
print() 
print()

# do_it()

lista_spadkowych_procentow : lista =[]
for element in downtrends:
        lista_spadkowych_procentow.append(get_change(element))


print(f"Mediana spadkow wynosi :: {mediana(lista_spadkowych_procentow)}")



lista_wzrostowych_procentow : lista =[]
for element in uptrends:
        lista_wzrostowych_procentow.append(get_change(element))


print(f"Mediana wzrostów wynosi :: {mediana(lista_wzrostowych_procentow)}")


        

# for element in 
