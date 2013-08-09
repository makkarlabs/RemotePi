#Flask Imports
from flask import Flask, jsonify, flash, request, redirect, url_for, session, abort

#App Imports
from RemotePi import app#, db
#from RemotePi.models import Role
import config

#Python Imports
import json

@app.route('/')
def index():
    return jsonify({"data":"yo"})

#You can write 'function decorators' like @login_required as shown below
#def subscription_required(fn):
#    @wraps(fn)
#    def decorated_view(*args, **kwargs):
#        print "subscribe"
#        if not is_subscribed(current_user):
#            return redirect('/subscribe')
#        return fn(*args, **kwargs)
#    return decorated_view

#def is_subscribed(user):
#    return User.query.filter_by(id=user.id).first().is_subscribed


