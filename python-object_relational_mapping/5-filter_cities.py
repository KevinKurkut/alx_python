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
query = ("SELECT cities.name "
         "FROM cities JOIN states ON cities.state_id = states.id "
         "WHERE states.name = %s "
         "ORDER BY cities.id ASC")
cur.execute(query)
"""# Fetch a rows """
results = cur.fetchall()
cities_list = ', '.join([row[0] for row in results])
print(cities_list)
"""close both database and cursor"""
cur.close()
conn.close()
