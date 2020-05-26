import json
from datetime import datetime

import django
import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=SYSCTA100_01_2020;UID=sa;PWD=sa')
cursor = conn.cursor()                        #Cursor Establishment
cursor.execute('select * from pv where z_id >= 830 order by z_id ')   #Execute Query

rs = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
cursor.connection.close()
for i in rs:
    print( i)