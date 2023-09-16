#!/usr/bin/python3
""" Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv


def main():
    """ The main function of the script"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    match = argv[4]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=database
        )
    cur = db.cursor()
    msg = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id ASC"
    sql_query = msg.format(match)
    cur.execute(sql_query)
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
