from flask import Flask, request, abort
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)

#New error response handler
def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response

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
            for row in query:
              result = row[slot]
        elif field == 'value' and int(slotId) >= 1 and int(slotId) <= 999:
            #return slot value
            slot = 'slot'
            slot += str(slotId)
            slot += '_value'
            query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
            for row in query:
              result = row[slot]
        elif field == 'units' and int(slotId) >= 1 and int(slotId) <= 999:
            #return slot units
            slot = 'slot'
            slot += str(slotId)
            slot += '_units'
            query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
            for row in query:
              result = row[slot]
        else:
            #return error
            #return {'error'}
            abort(404)

        result = { 'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


#Route_3
class Write(Resource):
    def get(self, roomId, slotId, field, value):
        conn = db_connect.connect()
        ## Check that room is in the valid int range
        if int(roomId) >=1 and int(roomId) <=999:
            if field == 'value' or field == 'name' or field == 'units':
                if int(slotId) >= 1 and int(slotId) <= 12:
                    slot = 'slot'
                    slot += str(slotId)
                    if field == 'value':
                        slot += '_value'
                    elif field == 'name':
                        slot += '_name'
                    else:
                        slot += '_units'
                    updatequery = conn.execute('update rooms set %s = \'%s\' where roomNum =%d' %(slot, value, int(roomId)))
                    lookupquery = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
                    for row in lookupquery:
                        #result = row[slot]
                        #result = { 'data': [dict(zip(tuple (lookupquery.keys()), i)) for i in lookupquery.cursor]}
                        result = { 'Data written to slot': row[slot] }
                        return jsonify(result)
                else:
                    return bad_request('Slot number out of range: ' + slotId)
            else:
                #print ('Invalid field: ' + field)
                #abort(404)
                return bad_request('Invalid field: ' + field)
        else:
            return bad_request('Room number out of range: ' + roomId)


api.add_resource(Rooms, '/rooms') # Route_1
api.add_resource(Room, '/rooms/<roomId>') # Route_2
api.add_resource(Read, '/rooms/<roomId>/<slotId>/read/<field>') # Route_3
api.add_resource(Write, '/rooms/<roomId>/<slotId>/write/<field>/<value>') # Route_4

if __name__ == '__main__':
    app.run(port=8002)
