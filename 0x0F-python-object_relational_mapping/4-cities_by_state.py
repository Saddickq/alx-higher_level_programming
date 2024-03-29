#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def main():
    """ Main function """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=database
    )
    cur = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON states.id = cities.state_id"
    cur.execute(sql)
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
