from flask import Flask
from downloader.db_function import DBSession
from downloader.models import Qingsongyike

app = Flask(__name__)

@app.route('/')
def index():
    session = DBSession()
    body = session.query(Qingsongyike.body).first()
    return body

if __name__ == '__main__':
    app.run()