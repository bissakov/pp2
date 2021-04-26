from connect import connect
from create_table import create_table
from insert import insert, insert_list
from update import update
from query import query, query_parts
from delete import delete

#connect()
#create_table()

# insert("3M Co.")
# sql = "INSERT INTO parts(part_name) VALUES(%s)"
# part_list = [
#     ('SIM Tray',),
#     ('Speaker',),
#     ('Vibrator',),
#     ('Antenna',),
#     ('Home Button',),
#     ('LTE Modem',)
# ]
# insert_list(sql,part_list)
#update(1, "ckjldkasjfl")

#query()
#query_parts()
# q = Query_fetchmany()
# q.query_part_vendors()

deleted_rows = delete(2)
print('The number of deleted rows: ', deleted_rows)
