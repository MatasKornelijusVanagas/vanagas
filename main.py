from math import sqrt
from math import pow

kintamasis = 1
kintamasis = 2

def funkcija():
    print(kintamasis)
    print(kintamasis2)
    print(F'test:{kintamasis2}{kintamasis}')
    print('test: {}{}'.format(kintamasis2, kintamasis))



pirmas = 4
antras = 6
def sudetis(pirmas,antras):
    return pirmas+antras

def atimtis(pirmas, antras):
    return pirmas-antras

def daugyba(pirmas, antras):
    return pirmas*antras

def dalyba(pirmas, antras):
    if antras == 0:
        return "Dalyba is nulio negalima"
    return pirmas / antras
    
def pakeltilaipsniu(pirmas,antras):
    return pow (pirmas, antras)

print("sudetis:", sudetis(pirmas, antras))
print("atimtis:", atimtis(pirmas, antras))
print("daugyba:", daugyba(pirmas, antras))
print("dalyba:", dalyba(pirmas, antras))
print("pakelta:", pakelimaslaipsniu(pirmas, antras))
