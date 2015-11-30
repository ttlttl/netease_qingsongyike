from . import db

class Qingsongyike(db.Model):
    __tablename__ = 'qingsongyike'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(32))
    docid = db.Column(db.String(32), unique=True)
    ptime = db.Column(db.String(32))
    cover_img = db.Column(db.String(512))
    url_3g = db.Column(db.String(512))
    body = db.Column(db.Text)