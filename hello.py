# pip install flask
# flask -app 'nombre archivo' run
# venv\Scripts\activate.bat

from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return "Hola ITE"


@app.route("/bye")
def adios():
    return "BYE BYE"
