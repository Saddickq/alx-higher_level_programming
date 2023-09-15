#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, port=3306, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
