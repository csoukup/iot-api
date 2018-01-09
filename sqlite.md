### Create new test.db
```
sqlite3 test.db
```
### DB Structure
Note: Need to determine how many slots to support and how to clear/reset
#### Rooms table:
| roomNum[numeric(3)] | slot1_name[varchar(25)] | slot1_value[varchar(25)] | slot1_units[varchar(10)] | ... |
| -- | -- | -- | -- | -- |
| 1 | Device 1 | 1 | '' | ... |
| 2 | Thermometer | 70 | F | ... |
| ... | ... | ... | ... | ... |
| 999 | Switch1 | on | '' | ... |

### Add rooms table and populate Room 1 with values
```
create table rooms(
  roomNum numeric(3) primary key,
  slot1_name varchar(25),
  slot1_value varchar(25),
  slot1_units varchar(10),
  slot2_name varchar(25),
  slot2_value varchar(25),
  slot2_units varchar(10),
  slot3_name varchar(25),
  slot3_value varchar(25),
  slot3_units varchar(10)
  ...
  slot12_name varchar(25),
  slot12_value varchar(25),
  slot12_units varchar(10));
insert into rooms values('1', '', '', '', '', '', '', '', '', '' ...);
insert into rooms values('2', '', '', '', '', '', '', '', '', '' ...);
insert into rooms values('3', '', '', '', '', '', '', '', '', '' ...);
...
insert into rooms values('999', '', '', '', '', '', '', '', '', '' ...);
.exit
```
