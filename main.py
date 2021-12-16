import json

import requests
from flask import Flask

app = Flask("API-Maurício")

@app.route("/pegarinfo", methods=["GET"])
def pegarinfo():
    a = response.status_code
    return {"nome":"Mauricio Helfstein Goncalves",
            "idade":"27 anos",
            "telefone":"(11)99106-2425"}

def get_simples(url):
    r = requests.get(url)
    return r

url_get = "http://127.0.0.1:5000/pegarinfo"

response = get_simples(url_get)
print(response.json())
print('Status code:',response.status_code)
app.run()