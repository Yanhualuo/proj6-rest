# Laptop Service
import os
import pymongo
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient


# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient("db", 27017)
db = client.tododb


#############################################

class ListAll(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]

        result = { 'open_time': [item["open_times"] for item in i],
        'close_time': [item["close_times"] for item in i],
        'km': [item["km"] for item in i]
        }
        return result


class ListAllJson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
        
        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        doc = []
        for item in i:
            item_doc = {
                'km': item["km"],
                'open_time' : item["open_times"],
                'close_time': item["close_times"]
            }
            doc.append(item_doc)
        return doc


class ListAllCsv(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
        
        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]

        result=[]
        
        for item in i:
            temp = item["km"] + ", " + item["open_times"] + ", " + item["close_times"]
            result.append(temp)
            
        return result



###################################################


class ListOpenOnly(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result = { 'open_time': [item["open_times"] for item in i]}
        return result

class ListOpenOnlyJson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100

        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result = []
        for item in i:
            item_doc = {
                'open_time' : item["open_times"]
            }
            result.append(item_doc)

        return result

class ListOpenOnlyCsv(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
    
        item_list = db.tododb.find().sort("open_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result=[]
        
        for item in i:
            temp = item["open_times"]
            result.append(temp)
        return result


#################################


class ListCloseOnly(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100
        item_list = db.tododb.find().sort("close_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result = { 'close_time': [item["close_times"] for item in i]}
        return result


class ListCloseOnlyJson(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100

        item_list = db.tododb.find().sort("close_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result = []
        for item in i:
            item_doc = {
                'close_time' : item["close_times"]
            }
            result.append(item_doc)
        return result


class ListCloseOnlyCsv(Resource):
    def get(self):
        top = request.args.get("top")
        if top == None:
            top = 100

        item_list = db.tododb.find().sort("close_times", pymongo.ASCENDING).limit(int(top))
        i = [item for item in item_list]
        
        result=[]
        
        for item in i:
            temp = item["close_times"]
            result.append(temp)

        return result


# Create routes

api.add_resource(ListAll, '/listAll')
api.add_resource(ListAllJson, '/listAllJson')
api.add_resource(ListAllCsv, '/listAllCsv')

api.add_resource(ListOpenOnly, '/listOpenOnly')
api.add_resource(ListOpenOnlyJson, '/listOpenOnlyJson')
api.add_resource(ListOpenOnlyCsv, '/listOpenOnlyCsv')

api.add_resource(ListCloseOnly, '/listCloseOnly')
api.add_resource(ListCloseOnlyJson, '/listCloseOnlyJson')
api.add_resource(ListCloseOnlyCsv, '/listCloseOnlyCsv')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
