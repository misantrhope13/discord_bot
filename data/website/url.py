from flask import Flask
from flask import render_template
import json

from data.parametrs.get_data import  list_1, list_2, list_3

app = Flask(__name__)


letters = []
for i in range(len(list_2)):
    letter = str(list_1[i]) + " " + list_2[i]+ " " + " " + str(list_3[i])

    letters.append(letter)


@app.route('/')
def odd_even():
    return render_template('index.html', letters=letters)



