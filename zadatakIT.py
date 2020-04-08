import hotel


lista_rezervacije=[]

suma=0.0

for i in range(4):
    i=0
    while(i<1):
        ime_prezime=input("Unesite ime i prezime: ")
        if ime_prezime=='':
            print("Ime ne moze biti prazno")
            i=0
        else:
            i=1    


    i=0
    while(i<1):
        br_dana=int(input("Unesite br dana: "))
        if br_dana<=0 or br_dana>366:
            print("Br dana nije dobar")
            i=0
        else:
            i=1   

    i=0
    while(i<1):
        br_kreveta=int(input("Unesite br kreveta: "))
        if br_kreveta<1 or br_kreveta>5:
            print("Nije dobar br kreveta")
            i=0
        else:
            i=1

    lista_rezervacije.append(hotel.rezervacija(ime_prezime,br_kreveta,br_dana))
    print("\n")
for l in lista_rezervacije:
    suma+=l

print("Zarada od rezervacija: ",round(suma,6)
)

gosti=hotel.gosti

for g in gosti:
    print(g)