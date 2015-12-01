from app import app, persistence
import random

def get_match_for_users(userList):
    matchList = []
    pendingAssign = list(userList)
    pendingMatch = list(userList)
    if len(userList) > 1:
        while len(pendingAssign):
            assignUser = random.choice(pendingAssign)
            matchUser = random.choice(pendingMatch)
            # reselect if we've picked ourselves
            while assignUser['id'] == matchUser['id']:
                matchUser = random.choice(pendingMatch)
            # add our match to list
            matchList.append({assignUser['id']:matchUser['id']})
            # remove from respective lists
            pendingAssign.remove(assignUser)
            pendingMatch.remove(matchUser)
        return matchList
    else:
        return None
        