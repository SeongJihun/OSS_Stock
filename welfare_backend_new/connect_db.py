import os

DATABASE_NAME = 'welfare'
DATABASE_USER = 'username'
DATABASE_PASSWORD = 'password'
DATABASE_PORT = 3306

DATABASE_URI = 'mysql+pymysql://{}:{}@welfare.cxapnigq6oij.ap-northeast-2.rds.amazonaws.com:{}/{}?charset=utf8'.format(
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_NAME
)