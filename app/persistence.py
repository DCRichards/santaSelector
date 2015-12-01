from app import app

userList = [];

def add_user(user):
    userList.append(user)
    
def get_users():
    return userList;
