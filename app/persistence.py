from app import app

userList = {}
matchList = {}
idIter = 0

def add_user(user):
    global idIter
    userList[idIter] = user
    idIter += 1
    
def remove_user(userId):
    del userList[userId]
    
def get_users():
    return userList

def get_user(user):
    try:
        return userList[user]
    except (KeyError, TypeError):
        return None

def get_match(user):
    try:
        return matchList[user]
    except (KeyError, TypeError):
        return None
    
def get_all_matches():
    return matchList

def add_matches(matches):
    global matchList
    matchList = matches
    