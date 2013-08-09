from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import logging
import config

app = Flask(__name__)
app.config.from_object('flask_app.config')
filehandler = logging.FileHandler(filename=config.LOG_FILE_LOC)
filehandler.setLevel(logging.INFO)
app.logger.addHandler(filehandler)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.DB_USERNAME + ':' + config.DB_PASSWORD + '@' + config.DB_SERVER + '/' + config.DB_NAME

db = SQLAlchemy(app)

from RemotePi import views
from RemotePi import models, forms
#import hedge_app.tasks

#Uncomment on server
#if __name__ == '__main__':
#    app.run()
