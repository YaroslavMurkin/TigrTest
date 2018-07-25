from flask import Flask, render_template
import random

weath = ['хреновая погода 2  градуса тепла и дождь',
           'тепло светло но ты поторопись 30 градусов тепла))',
           '    в антарктитде 30 можно играть в обморожение',
           'адская жара земля остановилась 3000 градусов тепла'
           ]


app = Flask(__name__)


@app.route('/tigr')
def index():
    return render_template('tigr.html')


@app.route('/menu')
def page1():
    return render_template('menu.html')


@app.route('/weather')
def weather():
    w = random.choice(weath)
    return render_template('weather.html', weather=w)

app.run(debug=True, port=8080)