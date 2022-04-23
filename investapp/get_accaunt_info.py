from investapp import create_app
from investapp.api_invest import get_accounts


app = create_app()
with app.app_context():
    get_accounts()

