from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import sys

db_connect = create_engine('sqlite:///test.db')
if not database_exists(db_connect.url):
    create_database(db_connect.url)

conn = db_connect.connect()
#Create rooms table with 12 slots per room
conn.execute(
    """create table rooms(roomNum numeric(3) primary key,
    slot1_name varchar(25),
    slot1_value varchar(25),
    slot1_units varchar(10),
    slot2_name varchar(25),
    slot2_value varchar(25),
    slot2_units varchar(10),
    slot3_name varchar(25),
    slot3_value varchar(25),
    slot3_units varchar(10),
    slot4_name varchar(25),
    slot4_value varchar(25),
    slot4_units varchar(10),
    slot5_name varchar(25),
    slot5_value varchar(25),
    slot5_units varchar(10),
    slot6_name varchar(25),
    slot6_value varchar(25),
    slot6_units varchar(10),
    slot7_name varchar(25),
    slot7_value varchar(25),
    slot7_units varchar(10),
    slot8_name varchar(25),
    slot8_value varchar(25),
    slot8_units varchar(10),
    slot9_name varchar(25),
    slot9_value varchar(25),
    slot9_units varchar(10),
    slot10_name varchar(25),
    slot10_value varchar(25),
    slot10_units varchar(10),
    slot11_name varchar(25),
    slot11_value varchar(25),
    slot11_units varchar(10),
    slot12_name varchar(25),
    slot12_value varchar(25),
    slot12_units varchar(10))""")

#Create 999 rooms
start = 1
stop = 1000

for x in range(start, stop):
    query = conn.execute('insert into rooms values(%d, \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\')' %(int(x)))
