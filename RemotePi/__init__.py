from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import logging
import config

app = Flask(__name__)
app.config.from_object('RemotePi.config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.DB_USERNAME + ':' + config.DB_PASSWORD + '@' + config.DB_SERVER + '/' + config.DB_NAME

#db = SQLAlchemy(app)

from RemotePi import views
#from RemotePi import models
#import hedge_app.tasks

#Uncomment on server
#if __name__ == '__main__':
#    app.run()
