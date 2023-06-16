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

def setRedisCache(name, phone, numberofexp):
    redis_db.set("name", name)
    redis_db.set("phone", phone)
    redis_db.set("numberofexp", numberofexp)
    return

def getRedisCache():
    name = redis_db.get("name")
    phone = redis_db.get("phone")
    numberofexp = redis_db.get("numberofexp")
    return {"name": name, "phone": phone, "numberofexp": numberofexp}

def deleteRedisCache():
    redis_db.delete("name")
    redis_db.delete("phone")
    redis_db.delete("numberofexp")
    return

def deleteAllDataFromRedis():
    redis_db.flushall()