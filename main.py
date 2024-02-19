from math import sqrt
from math import pow

kintamasis = 1
kintamasis2 = 2

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
print("pakelta:", pakeltilaipsniu(pirmas, antras))

while True:
    print("\nMatematiniai veiksmai:")
    print("1. Sudėtis")
    print("2. Atimtis")
    print("3. Daugyba")
    print("4. Dalyba")
    print("5. Pakelti laipsniu")
    print("0. Baigti darbą")
    
    pasirinkimas = input("Įvesti operaciją (1/2/3/4/5/0): ")
    
    if pasirinkimas in ['1', '2', '3', '4', '5']:
        pirmas_skaicius = float(input("Įvesti pirmą skaičių: "))
        antras_skaicius = float(input("Įvesti antrą skaičių: "))
        
        if pasirinkimas == '1':
            print("Rezultatas:", sudetis(pirmas_skaicius, antras_skaicius))
        elif pasirinkimas == '2':
            print("Rezultatas:", atimtis(pirmas_skaicius, antras_skaicius))
        elif pasirinkimas == '3':
            print("Rezultatas:", daugyba(pirmas_skaicius, antras_skaicius))
        elif pasirinkimas == '4':
            print("Rezultatas:", dalyba(pirmas_skaicius, antras_skaicius))
        elif pasirinkimas == '5':
            print("Rezultatas:", pakeltilaipsniu(pirmas_skaicius, antras_skaicius))
    elif pasirinkimas == '0':
        print("Programos darbas atliktas.")
        break
    else:
        print("Nėra tokio pasirinkimo. Bandyti dar kartą.")
