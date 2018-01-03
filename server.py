from flask import Flask, request, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

#Route_1
class Rooms(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from rooms") # This line performs query and returns json result
        return {'rooms': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Room ID

#Route_2
class Room(Resource):
    def get(self, roomId):
        conn = db_connect.connect()
        query = conn.execute("select * from rooms where roomNum =%d " %int(roomId))
        result = { 'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

#Route_3
class Read(Resource):
    def get(self, roomId, slotId, field):
        conn = db_connect.connect()
        if field == 'name' and int(slotId) >= 1 and int(slotId) <= 999:
            #return slot name
            slot = 'slot'
            slot += str(slotId)
            slot += '_name'
            print slot
            query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
        elif field == 'value' and int(slotId) >= 1 and int(slotId) <= 999:
            #return slot value
            slot = 'slot'
            slot += str(slotId)
            slot += '_value'
            query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
        elif field == 'units' and int(slotId) >= 1 and int(slotId) <= 999:
            #return slot units
            slot = 'slot'
            slot += str(slotId)
            slot += '_units'
            query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
        else:
            #return error
            #return {'error'}
            abort(404)

        result = { 'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Rooms, '/rooms') # Route_1
api.add_resource(Room, '/rooms/<roomId>') # Route_2
api.add_resource(Read, '/rooms/<roomId>/<slotId>/read/<field>') # Route_3
#api.add_resource(Write, '/rooms/<roomId>/<slotId>/write/<field>/<value>') # Route_4

if __name__ == '__main__':
    app.run(port=8002)
