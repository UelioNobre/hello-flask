from os import environ
from waitress import serve
from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)

joke_list = [
    "Por que o bombeiro não gosta de andar? <br> Porque ele socorre.",
    "Sabe como chama a sorveteria do Michel Teló? <br> Ice te Pego.",
    "Por que o espanador não luta caratê? <br> Porque ele luta capoeira",
]


@app.route("/api/joke")
def joke():
    return jsonify({"joke": random.choice(joke_list)})


@app.route("/api/users/random")
def users_random():
    user = requests.get("https://random-data-api.com/api/v2/users").json()
    print(user)
    return user


def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        # Servidor de desenvolvimento do Kit Werkzeug
        return app.run(debug=True, host=host, port=port)
    else:
        # Este é o waitress, otimizado para produção
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
