#!/usr/bin/python3
""" A module that connect a python script to the databases hbtn_0e_0_usa """
import MySQLdb
from sys import argv


def main():
    """ A function that selects all from the db hbtn_0e_0_usa """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            port=3306,
            db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
