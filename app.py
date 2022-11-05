from flask import Flask, request,jsonify
from flask_restful import Resource,Api
from flask_cors import CORS
from enum import Enum

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

class operation(Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"

class post_data(Resource):
    def post(self):
        result = 0
        data = request.get_json()
        operation_type = data.get("operation_type")
        x = data.get("x")
        y = data.get("y")

        addition = ["addition","add","plus","join"]
        subtraction = ["subtraction","subtract","minus","difference"]
        multiplication = ["multiplication","multiply","times","product"]

        operation_type = operation_type.split(" ")
        flag_add = 0
        flag_sub = 0
        flag_mul = 0

        for i in operation_type:
            for j in addition:
                if i==j:
                    flag_add = 1
                    break
            for j in subtraction:
                if i==j:
                    flag_sub = 1
                    break
            for j in multiplication:
                if i==j:
                    flag_mul = 1
                    break
        if flag_add == 1:
            result = x + y
            operation.value = "addition"
        
        elif flag_sub == 1:
            result = x - y
            operation.value = "subtraction"

        elif flag_mul == 1:
            result = x * y
            operation.value = "multiplication"


        

        result = {
            "slackUsername": "sandratoo", 
            "result": result, 
            "operation_type": operation.value 
                }

        return jsonify(result)

class getall(Resource):
    def get(self):
        all = jsonify({
            "slackUsername": "sandratoo", 
            "backend": True,
            "age": 28,
            "bio": "Hi, my name sandra, a curious and self-starting developer."
        })
        
        return all


api.add_resource(getall,"/")
api.add_resource(post_data,"/")

if __name__ == ("__main__"):
    app.run(debug=True)