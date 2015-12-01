from app import app, persistence
from flask import render_template, url_for, request
import json

@app.route('/')
def root():
    return render_template('index.html', users=persistence.get_users())

@app.route('/user', methods=['POST'])
def post():
    print json.loads(request.data)
    persistence.add_user(json.loads(request.data))
    return render_template('userlist.html', users=persistence.get_users())