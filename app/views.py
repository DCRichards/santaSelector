from app import app, persistence, match
from flask import render_template, url_for, request
import json

@app.route('/')
def root():
    return render_template('index.html', users=persistence.get_users())

@app.route('/user', methods=['POST'])
def post():
    user_dict = json.loads(request.data)
    persistence.add_user(user_dict)
    userList = persistence.get_users()
    print match.get_match_for_users(userList)
    return render_template('userlist.html', users=userList)

@app.route('/user/<int:id>', methods=['DELETE'])
def del_user():
    # Stub
    return None;

@app.route('/match/<int:id>', methods=['GET'])
def get():
    # Stub
    return None;

