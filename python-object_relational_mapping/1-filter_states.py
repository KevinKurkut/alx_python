"""importing modules"""
import MySQLdb
from sys import argv
"""open database communication"""
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
    )
cur = conn.cursor()
# execute SQL query using execute() method
query = "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8_bin ORDER BY id ASC;"
cur.execute(query)
"""# Fetch a rows """
results = cur.fetchall()
for row in results:
    print(row)
    """close both database and cursor"""
cur.close()
conn.close()
