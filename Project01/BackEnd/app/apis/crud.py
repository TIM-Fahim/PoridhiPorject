import json
from app import db
from models import Students
from app import redis_db

def inserting(name, phone, numberofexp):
    variable = Students(name=name, phone=phone, numberofexp=numberofexp)
    db.session.add(variable)
    db.session.commit()
    return variable.id

def deleting(id):
    student = Students.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return student
    else:
        return False
    
def updating(id, name):
    student = Students.query.get(id)
    if student:
        student.name = name
        db.session.commit()
        return Students.query.get(id)
    else:
        return False


def getAllData():
    return Students.query.all()

def getDataById(id):
    return Students.query.filter_by(id=id).first()

def setRedisCache(key, data):
    serialized_data = json.dumps(data)
    redis_db.set(key, serialized_data)

def getRedisCache(key):
    serialized_data = redis_db.get(key)
    if serialized_data is not None:
        data = json.loads(serialized_data)
        return data
    return None

def deleteRedisCache():
    redis_db.delete("name")
    redis_db.delete("phone")
    redis_db.delete("numberofexp")
    return

def deleteAllDataFromRedis():
    redis_db.flushall()