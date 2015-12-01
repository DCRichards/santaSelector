from app import app

userList = []
matchList = {}
id_iter = 0

def add_match(user, match):
    matchList[user] = match

def add_user(user):
    global id_iter
    user['id'] = id_iter
    id_iter += 1
    userList.append(user)
    
def get_users():
    return userList

def get_match(user):
    return matchList[user]

def get_all_matches():
    return matchList
