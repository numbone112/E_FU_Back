import json
from model.util import group
from model.db import mongo

# name,gender,birth,height,weight

def getpeople():
    return list(mongo.db.people.find({},{"_id":0}))

def addpeople(uid,name,gender,birth,height,weight):
    return list(mongo.db.people.insert_one({"uuid":uid,"name":name,"gender":gender,"birth":birth,"height":height,"weight":weight}))

def findname(name):
    return list(mongo.db.people.find({"name":name},{"_id":0}))

def finduid(uid):
    return list(mongo.db.people.find({"uuid":uid},{"_id":0}))

# def finduid(uid):
#     return list(mongo.db.people.find({"uid":uid},{"_id":0}))