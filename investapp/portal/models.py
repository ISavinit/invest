from investapp.db import db



class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ac_id = db.Column(db.Integer, unique=True)
    ac_type = db.Column(db.Integer)
    ac_name = db.Column(db.String(32), index=True, unique=True)
    ac_status = db.Column(db.String(10))
    ac_open = db.Column(db.DateTime)
    ac_close = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Account {self.name} {self.open}>'

