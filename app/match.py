from app import app
import random

def get_match_for_users(userList):
    matchList = {}
    pendingAssign = dict(userList)
    pendingMatch = dict(userList)
    if len(userList) > 1:
        while len(pendingAssign):
            assignUserKey = random.choice(pendingAssign.keys())
            matchUserKey = random.choice(pendingMatch.keys())
            # reselect if we've picked ourselves
            while assignUserKey == matchUserKey:
                matchUserKey = random.choice(pendingMatch.keys())
            # add our match to list
            matchList[assignUserKey] = matchUserKey
            # remove from respective lists
            del pendingAssign[assignUserKey]
            del pendingMatch[matchUserKey]
        return matchList
    else:
        return None
    