#!/usr/bin/python3
""" Write a script that lists all State objects from\
        the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """ main Function """
    usr = argv[1]
    password = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost/{}".format(usr, password, database)
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id)

        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as error:
        print(f"An error occurred: {error}")

    finally:
        session.close()


if __name__ == "__main__":
    main()
