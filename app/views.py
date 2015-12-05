from app import app, persistence, match
from flask import render_template, url_for, request, jsonify, Response
import json

def update_matches(userList):
    # update match list and store
    matches = match.get_match_for_users(userList)
    persistence.add_matches(matches)

@app.route('/')
def root():
    return render_template('index.html', users=persistence.get_users())

@app.route('/user', methods=['POST'])
def post():
    user_dict = json.loads(request.data)
    persistence.add_user(user_dict)
    userList = persistence.get_users()
    update_matches(userList)
    return render_template('userlist.html', users=userList), 201

@app.route('/user/<int:id>', methods=['DELETE'])
def del_user(id):
    persistence.remove_user(id)
    userList = persistence.get_users()
    update_matches(userList)
    return render_template('userlist.html', users=userList)

@app.route('/match/<int:id>', methods=['GET'])
def get(id):
    match = persistence.get_match(id)
    res_dict = {'%i' % id:match}
    # could be 0 so we need to specify None
    if match != None:
        return jsonify(**res_dict)
    else:
        return ('',404)
