from flask import render_template, Blueprint
from investapp.db import db
# from investapp.portal.models import Account

blueprint = Blueprint('portal', __name__)


@blueprint.route('/')
def index():
    title = "Инвестиционный портфель"
    # acc_list = Account.query.all()
    return render_template('portal/index.html', page_title=title)


