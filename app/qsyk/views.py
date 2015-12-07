from flask import render_template, request
from sqlalchemy import desc
from ..models import Qingsongyike
from . import qsyk

@qsyk.route('/qingsong')
def qingsong():
    page = request.args.get('page', 1, type=int)
    pagination = Qingsongyike.query.order_by(desc(Qingsongyike.ptime)).paginate(
        page, per_page=1, error_out=False
    )
    articles = pagination.items
    return render_template('qingsong.html', articles=articles, pagination=pagination)
