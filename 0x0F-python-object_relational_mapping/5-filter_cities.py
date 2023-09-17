#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and\
        lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def main():
    """ Main function """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
    )
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id WHERE states.name = %s"
    cur.execute(sql, (state,))
    query = cur.fetchall()
    city = ', '.join(row[0] for row in query)
    print(city)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
