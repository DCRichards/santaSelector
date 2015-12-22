from app import app, persistence, match
from flask import render_template, make_response, url_for, request, jsonify, Response
import json
import uuid

def update_matches(userList):
    # update match list and store
    matches = match.get_match_for_users(userList)
    persistence.add_matches(matches)
    
def generate_cookie():
    cookie_id = uuid.uuid4()
    #persistence.add_session(cookie_id)
    return cookie_id
    
@app.route('/')
def root():
    user_cookie = request.cookies.get('santaselector')
    if not user_cookie:
        user_cookie = generate_cookie()
        response = make_response(render_template('index.html', users=persistence.get_users()))
        response.set_cookie('santaselector', value=bytes(user_cookie))
        return response
    else:
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
    user = persistence.get_user(match)
    if match != None:
        return jsonify(**user)
    else:
        return ('',404)
