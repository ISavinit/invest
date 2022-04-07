from flask import url_for, render_template, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from investapp import db
from investapp.user.models import User
from investapp.user.forms import LoginForm, RegistrationForm

from flask import Blueprint

blueprint = Blueprint('portal', __name__, url_prefix='/')


@blueprint.route('/')
def portal():
    title = "Инвестиционный портфель"
    return render_template('portal/index.html', page_title=title)


