from application import db
from datetime import datetime


class Stock(db.Model):
    __tablename__ = 'stock'
    __tale_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock_name = db.Column(db.String(100), nullable=False)
    stock_category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, stock_name, stock_category, date):
        self.stock_name = stock_name
        self.stock_category = stock_category
        self.date = datetime.strptime(date, '%Y-%m-%d')

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

