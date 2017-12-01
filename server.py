from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

class Rooms(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from rooms") # This line performs query and returns json result
        return {'rooms': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Room ID

class Room(Resource):
    def get(self, roomId):
        conn = db_connect.connect()
        query = conn.execute("select * from rooms where roomId =%d " %int(roomId))
        result = { 'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Rooms, '/rooms') # Route_1
api.add_resource(Room, '/rooms/<roomId>') # Route_3


if __name__ == '__main__':
    app.run(port='8002')
