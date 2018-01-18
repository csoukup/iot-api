# iot-api
**IoT REST API**

## Initialize the DB
* python ./initialize_db.py

## Running the server
* python ./server.py

#### Listening server port
* The server runs on port 8002 (default)

http://\<server\>:8002/\<url\>

#### Functions:
\<url\>'s available
* List all rooms - /rooms
* List all slots and fields in a specific room - /rooms/\<roomId\>
* Read specific slot field in a specific room - /rooms/\<roomId\>/\<slotId\>/read/\<field\>
* Write specific slot field in a specific room - /rooms/\<roomId\>/\<slotId\>/write/\<field\>/\<value\>

#### Rooms:
* 1-999

#### Slots:
* 1-12

#### Values:
* name
* value
* units

---

### Examples:
* List all rooms 
```
http://127.0.0.1:8002/rooms
    GET /rooms
```
* List all slot values for room 5
```
http://127.0.0.1:8002/rooms/5
    GET /rooms/5
```
* Write name to room 5, slot1_name
```
http://127.0.0.1:8002/rooms/5/1/write/name/Thermometer
    GET /rooms/5/1/write/name/Thermometer
```
* Write value to room 5, slot1_value
```
http://127.0.0.1:8002/rooms/5/1/write/value/55
    GET /rooms/5/1/write/value/55
```
* Write units to room 5, slot1_units
```
http://127.0.0.1:8002/rooms/5/1/write/units/F
    GET /rooms/5/1/write/units/F
```
* Read name to room 5, slot1_name
```
http://127.0.0.1:8002/rooms/5/1/read/name
    GET /rooms/5/1/read/name
```
* Read value to room 5, slot1_value
```
http://127.0.0.1:8002/rooms/5/1/read/value
    GET /rooms/5/1/read/value
```
* Read units to room 5, slot1_units
```
http://127.0.0.1:8002/rooms/5/1/read/units
    GET /rooms/5/1/read/units
```
