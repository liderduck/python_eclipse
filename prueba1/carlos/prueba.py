
'''
Created on 5/2/2016

@author: jonathan
'''
def costo_hotel(noches):
    return 140*noches

def costo_del_vuelo(ciudad):
    if ciudad=="C�rdoba":
        return 821
    elif ciudad=="Iguaz�":
        return 941
    elif ciudad=="Ushuaia":
        return 1280
    elif ciudad=="Bariloche":
        return 1848

coste = costo_del_vuelo("C�rdoba")
print (coste)