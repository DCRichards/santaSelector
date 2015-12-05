from app import app

userList = {}
matchList = {}
idIter = 0

def add_match(user, match):
    matchList[user] = match

def add_user(user):
    global idIter
    userList[idIter] = user
    idIter += 1
    
def remove_user(userId):
    del userList[userId]
    
def get_users():
    return userList

def get_match(user):
    return matchList[user]

def get_all_matches():
    return matchList
