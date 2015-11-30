from flask import render_template
from ..models import Qingsongyike
from . import qsyk

@qsyk.route('/qsyk')
def qsyk():
    qingsongyike=Qingsongyike.query[-1]
    title=qingsongyike.title
    body=qingsongyike.body
    return render_template('qsyk.html',title=title, body=body)
