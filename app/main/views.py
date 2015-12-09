from flask import render_template
from . import main
from .weather import weather

@main.route('/')
def index():
    return render_template('index.html', weather=weather)
