from pkgutil import get_data
from app import app
from flask import request, jsonify
import json
from app.apis.crud import deleteAllDataFromRedis, getRedisCache, inserting, getAllData, setRedisCache

# by defaul it will be GET method
@app.route("/")
def index():
    return "Connected to app server;"

@app.route("/create", methods=["POST"])
def insertDataToDB():
    payload = request.get_json()
    name = payload["name"]
    phone = payload["phone"]
    numberofexp = payload["numberofexp"]
    if name and phone and numberofexp:
        res = inserting(name, phone, numberofexp)
        if res:
            return jsonify({"student inserted success fully. id": res}), 201
    else:
        return jsonify({"Please provide all the required fields"}), 400
    
    # students = getAllData()
    # serialized_students = [student.serialize() for student in students]
    # return jsonify({'message': 'success', 'data': serialized_students}), 200

@app.route("/getall", methods=["GET"])
def getDataFromDB():
    try:
        res = getRedisCache()
        if res:
            return jsonify({'message': 'success', 'isCached': 'yes', 'data': res}), 200

        students = getAllData()
        serialized_students = [student.serialize() for student in students]
        data = []
        for student in serialized_students:
            data.append({'name': student['name'], 'phone': student['phone'], 'numberofexp': student['numberofexp']})

        setRedisCache(json.dumps(serialized_students))
        return jsonify({'message': 'success', 'isCached': 'No', 'data': data}), 200

    except Exception as e:
        return jsonify({'message': 'error', 'error': str(e)}), 500



# @app.route("/deleteallredis", methods=["DELETE"])
# def getDataFromDB():
#         deleteAllDataFromRedis()
#         return jsonify({'message': 'success', 'data': 'deleted'}), 200