import os
from Voyageurs import Voyageurs
from Train import Train

Quai = []

def remplirquai(generator):
    """fonction itérant sur le genérateur passé en paramètre et remplissant la liste Quai d'objet voyageurs """
    for numbers in generator:
        voya = Voyageurs(numbers)
        Quai.append(voya)
    
remplirquai(range(1, 111))
print(Quai)
 
Train150 = Train()
placestrain = []

for keys in Train150.PLACES:
    placestrain.append(keys)

for passagers, places in zip(Quai,placestrain):
    passagers.place = places

couples = []
for elem in zip(placestrain, Quai):
    couples.append(elem)


for elem in couples:
    for keys in Train150.PLACES.keys():
        if elem[0] == keys:
            Train150.PLACES[elem[0]] = elem[1]
for values in Train150.PLACES.values():
    if values in Quai:
        Quai.remove(values)

print(Train150.PLACES)
print(Quai)