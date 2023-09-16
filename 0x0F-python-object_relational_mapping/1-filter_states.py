#!/usr/bin/python3
""" A script that lists all states with a name starting with N (upper N) \
        from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


def main():
    """ The main function of the script """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            port=3306,
            host='localhost',
            db=database
    )
    sql = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur = db.cursor()
    cur.execute(sql)
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
