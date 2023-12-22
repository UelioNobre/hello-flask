from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "Hello world!"


@app.route("/api")
def hello_word_api_json():
    return jsonify({"message": "Ola mundo com Flask e JSON!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
