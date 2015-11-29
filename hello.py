from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from downloader.db_function import DBSession
from downloader.models import Qingsongyike

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session = DBSession()
    qingsongyike = session.query(Qingsongyike).first()
    session.close()
    title=qingsongyike.title
    body=qingsongyike.body
    return render_template('index.html',title=title, body=body)

if __name__ == '__main__':
    manager.run()