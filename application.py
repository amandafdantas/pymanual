from flask import Flask, render_template


application = Flask(__name__)


@application.route('/')
def main(): #metodo main abre o index.html
    return render_template('index.html')