from flask import Flask, render_template
from data.function.func import letters_1, letters_2


app = Flask(__name__)


@app.route('/year/1')
def year_1():
    return render_template('index.html', letters=letters_1)


@app.route('/year/2')
def year_2():
    return render_template('index.html', letters=letters_2)


