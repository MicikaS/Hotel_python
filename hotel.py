gosti=[]

def rezervacija(gost,br_kreveta,br_dana):
    cena = 22.6*br_dana + 4.14*br_kreveta
    print("Za gosta: " ,gost, " cena rezervacije iznosi: ",round(cena,6))
    novi={
        "gost":[br_kreveta,br_dana]

    }
    gosti.append(novi) 
    return cena

