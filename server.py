from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/meteo')
def meteo():
    response = requests.get('https://wttr.in/Milano?format=j1')
    dati = response.json()
    
    temp = dati['current_condition'][0]['temp_C']
    descrizione = dati['current_condition'][0]['weatherDesc'][0]['value']    
    return jsonify({
        'temperatura': temp,
        'condizione': descrizione
    })

if __name__ == '__main__':
    app.run()