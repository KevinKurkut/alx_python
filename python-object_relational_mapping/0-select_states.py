"""MySQLdb is an interface for connecting to 
a MySQL database server from Python."""
import MySQLdb
"""open database communication"""
db = MySQLdb.connect("localhost", "root", "Chebiemitform3", "hbtn_0e_0_usa")
# prepare a cursor object using cursor() method
cursor = db.cursor()

query = "SELECT * FROM states ORDER BY id ASC;"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
            print(row)
