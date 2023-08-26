"""importing modules"""
import MySQLdb
from sys import argv
"""open database communication"""
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    charset="utf8"
    )
cur = conn.cursor()
# execute SQL query using execute() method
cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC" (argv[4], ))
"""# Fetch a rows """
results = cur.fetchall()
for row in results:
    if row[1].startswith("N"):
        print(row)
"""close both database and cursor"""
cur.close()
conn.close()
