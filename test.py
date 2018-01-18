from sqlalchemy import create_engine
import sys

db_connect = create_engine('sqlite:///test.db')

operation = sys.argv[1]

if operation == 'read':
    #python test.py read <roomId> <slotId> <field>
    roomId = sys.argv[2]
    slotId = sys.argv[3]
    field = sys.argv[4]

    conn = db_connect.connect()

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
        query = conn.execute('select %s from rooms where roomNum =%d' %(slot, int(roomId)))
        for row in query:
            result = row[slot]
    else:
        print ('Invalid field: ' + field)
        sys.exit(1)

    print ('room : ' + roomId)
    print ('slot : ' + slot)
    print ('result : ' + result)

elif operation == 'write':
    #python test.py write <roomId> <slotId> <field> <value>
    roomId = sys.argv[2]
    slotId = sys.argv[3]
    field = sys.argv[4]
    value = sys.argv[5]

    conn = db_connect.connect()

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
          result = row[slot]

    else:
        print ('Invalid field: ' + field)
        sys.exit(1)


    print ('room : ' + roomId)
    print ('slot : ' + slot)
    print ('result : ' + result)
