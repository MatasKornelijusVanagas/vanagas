from flask import Flask, request
from math import pow  # eksponentine funkcija

app = Flask(__name__)

# aritmetines operacijos
def sudetis(pirmas, antras):
    return pirmas + antras

def atimtis(pirmas, antras):
    return pirmas - antras

def daugyba(pirmas, antras):
    return pirmas * antras

def dalyba(pirmas, antras):
    if antras == 0:
        return "Dalyba iš nulio negalima"
    return pirmas / antras

def pakeltilaipsniu(pirmas, antras):
    return pow(pirmas, antras)

@app.route("/")  # operaciju forma
def home():
    return '''
            <form action="/calculate" method="get">
                <label for="pirmas">Įveskite pirmą skaičių:</label><br>
                <input type="text" id="pirmas" name="pirmas" value="0"><br><br>
                
                <label for="antras">Įveskite antrą skaičių:</label><br>
                <input type="text" id="antras" name="antras" value="0"><br><br>
                
                <label for="operacija">Pasirinkite operaciją:</label><br>
                <select name="operacija" id="operacija">
                    <option value="sudetis">Sudėtis</option>
                    <option value="atimtis">Atimtis</option>
                    <option value="daugyba">Daugyba</option>
                    <option value="dalyba">Dalyba</option>
                    <option value="pakelti">Pakelti laipsniu</option>
                </select><br><br>

                <input type="submit" value="Skaičiuoti">
            </form> 
            '''

@app.route("/calculate")  # atlikimas operaciju webe
def calculate():
    pirmas_skaicius = request.args.get("pirmas", default=0, type=float)
    antras_skaicius = request.args.get("antras", default=0, type=float)
    operacija = request.args.get("operacija")

    if operacija == "sudetis":
        result = sudetis(pirmas_skaicius, antras_skaicius)
    elif operacija == "atimtis":
        result = atimtis(pirmas_skaicius, antras_skaicius)
    elif operacija == "daugyba":
        result = daugyba(pirmas_skaicius, antras_skaicius)
    elif operacija == "dalyba":
        result = dalyba(pirmas_skaicius, antras_skaicius)
    elif operacija == "pakelti":
        result = pakeltilaipsniu(pirmas_skaicius, antras_skaicius)
    else:
        return "Neteisinga operacija"

    return f"Operacijos rezultatas: {result}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
