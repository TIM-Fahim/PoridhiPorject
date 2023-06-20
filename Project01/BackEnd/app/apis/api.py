from pkgutil import get_data
from app import app
from flask import request, jsonify
import json
from app.apis.crud import deleteAllDataFromRedis, deleting, getDataById, getRedisCache, inserting, getAllData, setRedisCache, updating

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
    
    
# @app.route("/getlist", methods=["GET"])
# def getDataFromDB():
#         students = getAllData()
#         serialized_students = [student.serialize() for student in students]
#         data = []
#         for student in serialized_students:
#             data.append({'id': student['id'], 'name': student['name'], 'phone': student['phone'], 'numberofexp': student['numberofexp']})
#         return jsonify({'message': 'success', 'isCached': 'No', 'data': data}), 200

import redis
from flask import jsonify


@app.route("/getlist", methods=["GET"])
def getDataFromDB():
    # Check if data is cached in Redis
    cached_data = getRedisCache("student_data")
    if cached_data:
        # Data found in Redis cache, return it
        return jsonify({'message': 'success', 'isCached': 'Yes', 'data': cached_data}), 200

    # Data not found in Redis cache, fetch from the database
    students = getAllData()
    serialized_students = [student.serialize() for student in students]
    data = []
    for student in serialized_students:
        data.append({'id': student['id'], 'name': student['name'], 'phone': student['phone'], 'numberofexp': student['numberofexp']})

    # Cache the data in Redis for future requests
    setRedisCache("student_data", data)

    return jsonify({'message': 'success', 'isCached': 'No', 'data': data}), 200


@app.route("/delete", methods=["DELETE"])
def deleteDataFromDB():
    payload = request.get_json()
    id = payload["id"]
    
    if id:
        res = deleting(id)
        if res:
            return jsonify({"student deletion successfully": res.serialize()}), 201
        else:
            return jsonify({"Cannot find any student with the id": id}), 400

    else:
        return jsonify({"Please Provide an ID to delete"}), 400



@app.route("/update", methods=["PUT"])
def updateDatafromDB():
    payload = request.get_json()
    id = payload["id"]
    name = payload["name"]
    if id and name:
        res = updating(id, name)
        if res:
            return jsonify({"student update successfully": res.serialize()}), 201
        else:
            return jsonify({"Cannot find any student with the id": id}), 400

    else:
        return jsonify({"Please Provide an ID and Name to udpate"}), 400



@app.route("/getbyid", methods=["GET"])
def getSingleDataFromDB():
        payload = request.get_json()
        id = payload["id"]
        if id:

            res = getDataById(id)
            if res:
                return jsonify({"student": res.serialize()}), 201
            else:
                return jsonify({"Cannot find any student with the id": id}), 400
        else:
            return jsonify({"Please Provide an ID to get"}), 400

# @app.route("/getall", methods=["GET"])
# def getDataFromDB():
#     try:
#         res = getRedisCache()
#         if res:
#             return jsonify({'message': 'success', 'isCached': 'yes', 'data': res}), 200

#         students = getAllData()
#         serialized_students = [student.serialize() for student in students]
#         data = []
#         for student in serialized_students:
#             data.append({'name': student['name'], 'phone': student['phone'], 'numberofexp': student['numberofexp']})

#         setRedisCache(json.dumps(serialized_students))
#         return jsonify({'message': 'success', 'isCached': 'No', 'data': data}), 200

#     except Exception as e:
#         return jsonify({'message': 'error', 'error': str(e)}), 500
    
  

# @app.route("/deleteallredis", methods=["DELETE"])
# def getDataFromDB():
#         deleteAllDataFromRedis()
#         return jsonify({'message': 'success', 'data': 'deleted'}), 200