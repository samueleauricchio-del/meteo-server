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
    import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
