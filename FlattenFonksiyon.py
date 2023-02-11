liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
YeniListe = []

for i in liste:
    print(isinstance(i, list))

def duzlestir(liste):
    for i in liste:
        if isinstance(i, list):
            duzlestir(i)
        else:
            YeniListe.append(i)


duzlestir(liste)
print(YeniListe)
