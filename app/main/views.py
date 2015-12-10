from flask import render_template
from . import main
from .weather import get_weather

@main.route('/')
def index():
    weather = get_weather('shanghai')
    return render_template('index.html', weather=weather)
